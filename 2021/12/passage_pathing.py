#%%
import numpy as np
import pandas as pd
from io import StringIO
from time import perf_counter

example = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

example2 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

# paths = np.genfromtxt(StringIO(example), delimiter="-", dtype=str)
# paths = np.genfromtxt(StringIO(example2), delimiter="-", dtype=str)
paths = np.genfromtxt("input.txt", delimiter="-", dtype=str)
unique = np.unique(paths)

adjacency = {
    k: np.concatenate([paths[paths[:, 0] == k, 1], paths[paths[:, 1] == k, 0]])
    for k in unique
}

# %% part 1

start = perf_counter()


def discover(path_list):
    global path_counter

    for e in adjacency[path_list[-1]]:
        if not e.isupper() and e in path_list:
            continue
        if e == "end":
            path_counter = path_counter + 1
            # print([*path_list, e])
            continue
        discover([*path_list, e])


path_counter = 0
discover(["start"])
print(f"Paths Found: {path_counter}")
print(f"Runtime = {perf_counter()-start}")

# %% part 2, really slow

start = perf_counter()


def discover_p2(path_list, small_cave):
    global path_counter

    for e in adjacency[path_list[-1]]:
        if e == "start":
            continue

        e_small_cave = small_cave
        if not e.isupper() and e in path_list:
            if e_small_cave is None:
                e_small_cave = e
            else:
                continue
        if e == "end":
            path_counter = path_counter + 1
            continue
        discover_p2([*path_list, e], e_small_cave)


path_counter = 0
discover_p2(["start"], None)
print(f"Paths Found Part 2: {path_counter}")
print(f"Runtime = {perf_counter()-start}")
# %%
