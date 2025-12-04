# %%
import time

with open("input.txt") as f:
    data = [list(x) for x in f.read().strip().split("\n")]
# %%
offsets = [[1, 1], [0, 1], [-1, 1], [1, 0], [-1, 0], [1, -1], [0, -1], [-1, -1]]


def countAdjacent(data, x, y):
    adjacent = 0
    for ox, oy in offsets:
        dx = x + ox
        dy = y + oy
        adjacent += (
            0 <= dx < len(data) and 0 <= dy < len(data[0]) and data[dx][dy] == "@"
        )
    return adjacent


result = sum(
    countAdjacent(data, x, y) < 4
    for x in range(len(data))
    for y in range(len(data[0]))
    if data[x][y] == "@"
)

print(f"Part1: {result}")  # 1569

# %%

grid = [x.copy() for x in data]


def removePaper(grid):
    removed = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] != "@":
                continue
            if countAdjacent(grid, x, y) < 4:
                grid[x][y] = "x"
                removed += 1

    return removed


start = time.time()
result = 0
while True:
    n = removePaper(grid)
    if n == 0:
        break
    result += n

print(f"Part2: {result} Execution Time: {time.time() - start:.3f}s")  # 9280

# %%
