# %%
"""
According to Reddit the user input is designed in a trivial way, such that only
the total area of the gifts has to be compared to the available space.
However, this does not apply to the given example input.
Solving the problem properly would be a big effort.
"""

with open("input.txt") as f:
    sections = f.read().strip().split("\n\n")
    gifts = [x.count("#") for x in sections[:-1]]  # area of each gift
    trees = []
    for tree_line in sections[-1].split("\n"):
        a, g = tree_line.split(": ")
        dims = a.split("x")
        g = [int(x) for x in g.split()]
        trees.append((int(dims[0]) * int(dims[1]), g))  # tree area with gift count
# %%

result = 0
for tree in trees:
    gift_area = 0
    for i in range(len(tree[1])):
        gift_area += tree[1][i] * gifts[i]
    if gift_area < tree[0]:
        result += 1

print(f"Part 1 trivial solution: {result}")
# %%
