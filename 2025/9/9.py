# %%
with open("input.txt") as f:
    tiles = [[int(x) for x in line.split(",")] for line in f.read().strip().split("\n")]
# %%
max_area = 0
for i in range(len(tiles) - 1):
    for j in range(i + 1, len(tiles)):
        dx = abs(tiles[i][0] - tiles[j][0]) + 1
        dy = abs(tiles[i][1] - tiles[j][1]) + 1
        area = dx * dy
        if max_area < area:
            max_area = area

print(f"Part 1: {max_area}")  # 4761736832
# %% Part 2: compress grid to only existing coordinates
coord_x = set()
coord_y = set()
for y, x in tiles:
    coord_x.add(x)
    coord_y.add(y)
coord_x = sorted(list(coord_x))
coord_y = sorted(list(coord_y))
# note: create an emtpy border of size 1 to floodfill the border around the closed shape
coord_to_grid_x = {coord_x[i]: i + 1 for i in range(len(coord_x))}
coord_to_grid_y = {coord_y[i]: i + 1 for i in range(len(coord_y))}
grid = [["." for _ in range(len(coord_y) + 2)] for _ in range(len(coord_x) + 2)]


def convertTile(tile: tuple):
    return coord_to_grid_x[tile[1]], coord_to_grid_y[tile[0]]


def increment(x1, x2):
    if x1 < x2:
        return 1
    if x1 > x2:
        return -1
    return 0


# fill path from tile coordinates
for i in range(len(tiles)):
    x1, y1 = convertTile(tiles[i - 1])
    x2, y2 = convertTile(tiles[i])
    grid[x1][y1] = "X"
    while x1 != x2 or y1 != y2:
        x1 += increment(x1, x2)
        y1 += increment(y1, y2)
        grid[x1][y1] = "X"

# floodfill boundary layer from (0,0)
next_cells = [(0, 0)]
while next_cells:
    x, y = next_cells.pop()
    grid[x][y] = "#"
    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        if (
            0 <= x + dx < len(grid)
            and 0 <= y + dy < len(grid[0])
            and grid[x + dx][y + dy] == "."
        ):
            next_cells.append((x + dx, y + dy))


def checkPath(x, y, x2, y2):
    while x != x2:
        x += increment(x, x2)
        if grid[x][y] == "#":
            return False
    while y != y2:
        y += increment(y, y2)
        if grid[x][y] == "#":
            return False
    return True


# if the full border is included (red/green tiles), the area must valid
def verifyArea(tile1: tuple, tile2: tuple):
    x1, y1 = convertTile(tile1)
    x2, y2 = convertTile(tile2)
    if not checkPath(x1, y1, x2, y2):
        return False
    if not checkPath(x2, y2, x1, y1):
        return False
    return True


max_area = 0
for i in range(len(tiles) - 1):
    for j in range(i + 1, len(tiles)):
        dx = abs(tiles[i][0] - tiles[j][0]) + 1
        dy = abs(tiles[i][1] - tiles[j][1]) + 1
        area = dx * dy
        if max_area < area and verifyArea(tiles[i], tiles[j]):
            max_area = area

print(f"Part 2: {max_area}")  # 1452422268
