#%%

with open("input.txt") as f:
    rules, updates = f.read().strip().split("\n\n")
    rules = rules.split("\n")
    updates = updates.split("\n")
    rules = [(int(x.split("|")[0]), int(x.split("|")[1])) for x in rules]
    updates = [[int(x) for x in y.split(",")] for y in updates ]
# %%

result = 0
for update in updates:
    indices = {update[i]:i for i in range(len(update))}
    valid = True
    for p in update:
        for rule in rules:
            if rule[0] == p and indices[p] > indices.get(rule[1], 1e6):
                valid = False
        
    if valid:
        result += update[len(update)//2]

print(f"Part 1: {result}") # 6619 too high

# %%
