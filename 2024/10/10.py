# %%
with open("input.txt") as f:
    data = f.readlines()
    topography = [[int(x) for x in line.strip()] for line in data]
    print(topography)
# %%
dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def findPaths(start):
    nodes = [start]
    paths = set()
    paths_count = 0
    while nodes:
        current = nodes.pop()
        if topography[current[0]][current[1]] == 9:
            paths.add((current[0], current[1]))
            paths_count += 1
            continue

        for d in dirs:
            next_x = current[0] + d[0]
            next_y = current[1] + d[1]
            if (
                0 <= next_x < len(topography)
                and 0 <= next_y < len(topography[0])
                and topography[current[0]][current[1]] + 1 == topography[next_x][next_y]
            ):
                nodes.append([next_x, next_y])
    return len(paths), paths_count


res1 = 0
res2 = 0
for x in range(len(topography)):
    for y in range(len(topography[0])):
        if topography[x][y] == 0:
            p1, p2 = findPaths([x, y])
            res1 += p1
            res2 += p2
print(f"Part1: {res1}, Part2: {res2}")
# %%
