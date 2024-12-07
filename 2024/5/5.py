# %%
with open("input.txt") as f:
    rules, updates = f.read().strip().split("\n\n")
    rules = rules.split("\n")
    updates = updates.split("\n")
    rules = [(int(x.split("|")[0]), int(x.split("|")[1])) for x in rules]
    updates = [[int(x) for x in y.split(",")] for y in updates]


# %%
def isValid(update):
    indices = {update[i]: i for i in range(len(update))}
    valid = True
    for p in update:
        for rule in rules:
            if rule[0] == p and indices[p] > indices.get(rule[1], 1e6):
                valid = False
                break
    return valid


result = sum(update[len(update) // 2] for update in updates if isValid(update))
print(f"Part 1: {result}")  # 6619 too high

# %%
result = 0
updates_sorted = [x.copy() for x in updates]
for update in updates_sorted:
    indices = {update[i]: i for i in range(len(update))}
    wasSorted = False
    while not isValid(update):
        wasSorted = True
        for i in range(len(update)):
            for rule in rules:
                if rule[0] == update[i] and i > indices.get(rule[1], 1e6):
                    update[i], update[indices.get(rule[1])] = (
                        update[indices.get(rule[1])],
                        update[i],
                    )
                    indices[rule[0]], indices[rule[1]] = (
                        indices[rule[1]],
                        indices[rule[0]],
                    )

    if wasSorted:
        result += update[len(update) // 2]

print(f"Part 2: {result}")

# %%
