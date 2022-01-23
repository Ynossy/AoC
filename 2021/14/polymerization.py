#%%
import numpy as np

# with open("example.txt") as f:
with open("input.txt") as f:
    data = f.read().splitlines()

template = data[0]

pairs = {x.split(" -> ")[0]: x.split(" -> ")[1] for x in data[2:]}

#%% build new strings
polymer = template
for i in range(10):
    print(f"round {i}")
    grow = polymer[0]
    for i in range(len(polymer) - 1):
        if polymer[i : i + 2] in pairs:
            grow += pairs[polymer[i : i + 2]]
        grow += polymer[i + 1]
    polymer = grow

counts = [
    polymer.count("N"),
    polymer.count("C"),
    polymer.count("H"),
    polymer.count("B"),
]

print(f"Result: {max(counts)-min(counts)}")
# %% part 2 - optimize
import copy
from time import perf_counter

start = perf_counter()

split = np.array([x.split(" -> ") for x in data[2:]])
pairs_post = {x[0]: [x[1], 0] for x in split}


for i in range(len(template) - 1):
    if template[i : i + 2] in pairs_post:
        pairs_post[template[i : i + 2]][1] += 1

count = {x: template.count(x) for x in set(split[:, 1])}

for _ in range(40):
    pairs_pre = copy.deepcopy(pairs_post)  # need to copy the dict and its values
    for pair, (element, _) in pairs_pre.items():
        count[element] += pairs_pre[pair][1]
        pairs_post[pair][1] -= pairs_pre[pair][1]
        pairs_post[pair[0] + element][1] += pairs_pre[pair][1]
        pairs_post[element + pair[1]][1] += pairs_pre[pair][1]


max_letter = max(count, key=count.get)
min_letter = min(count, key=count.get)

print(f"Runtime = {perf_counter()-start}")
print(f"Result: {count[max_letter]-count[min_letter]}")
# %%
