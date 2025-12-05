# %%

with open("input.txt") as f:
    ranges, ingredients = f.read().strip().split("\n\n")
    ingredients = [int(x) for x in ingredients.strip().split("\n")]
    ranges = [[int(x) for x in y.split("-")] for y in ranges.strip().split("\n")]
# %%


def inRange(n):
    for low, high in ranges:
        if low <= n <= high:
            return True
    return False


result = sum(inRange(n) for n in ingredients)

print(f"Part 1: {result}")  # 525
# %%

new_ranges = []

for r_low, r_high in ranges:
    cut_upper = -1
    cut_lower = -1
    remove = []
    for i in range(len(new_ranges)):
        nr_low, nr_high = new_ranges[i]
        if nr_low <= r_low <= nr_high:
            cut_lower = i
        if nr_low <= r_high <= nr_high:
            cut_upper = i
        # fully included, delete these ranges afterwards
        if r_low < nr_low and nr_high < r_high:
            remove.append(i)
    if cut_upper == -1 and cut_lower == -1:
        # not intersecting any range --> add
        new_ranges.append([r_low, r_high])
    elif cut_upper != -1 and cut_lower == -1:
        # intersecting on upper end --> extend exisiting
        new_ranges[cut_upper][0] = r_low
    elif cut_upper == -1 and cut_lower != -1:
        # intersecting on lower end --> extend exisiting
        new_ranges[cut_lower][1] = r_high
    elif cut_upper != -1 and cut_lower != -1 and cut_upper != cut_lower:
        # intersecting on lower and upper end --> merge 2 ranges
        new_ranges[cut_lower][1] = new_ranges[cut_upper][1]
        remove.append(cut_upper)
    remove.sort(reverse=True)
    for r in remove:
        new_ranges.pop(r)

result = sum(upper - lower + 1 for lower, upper in new_ranges)

print(f"Part 2: {result}")  # 333892124923577
# %%
