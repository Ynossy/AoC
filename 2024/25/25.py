#%%
with open("input.txt") as f:
    data = f.read().strip().split("\n\n")
    keys = []
    locks = []
    for d in data:
        lines = d.splitlines()
        counts = [-1 for _ in range(len(lines[0]))]
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if lines[i][j] == '#':
                    counts[j] += 1
        if '.' in lines[0]:
            keys.append(tuple(counts))
        else:
            locks.append(tuple(counts))

res = 0

for key in keys:
    for lock in locks:
        if all(key[i] + lock[i] <= 5 for i in range(len(key))):
            res += 1
print(f"Part 1: {res}")

# %%
