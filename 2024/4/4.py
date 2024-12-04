# %%

with open("input.txt") as f:
    grid = [list(x.strip()) for x in f.readlines()]
# %%
horizontal = [[0, 0], [1, 0], [2, 0], [3, 0]]
vertical = [[0, 0], [0, 1], [0, 2], [0, 3]]
dia1 = [[0, 0], [1, 1], [2, 2], [3, 3]]
dia2 = [[0, 0], [1, -1], [2, -2], [3, -3]]


def findXmas(grid, direction):
    count = 0
    len_x = len(grid)
    len_y = len(grid[0])
    for x in range(len_x):
        for y in range(len_y):
            if (
                0 <= x + direction[-1][0] < len_x
                and 0 <= y + direction[-1][1] < len_x
                and (
                    all(
                        grid[x + direction[k][0]][y + direction[k][1]] == "XMAS"[k]
                        for k in range(4)
                    )
                    or all(
                        grid[x + direction[k][0]][y + direction[k][1]] == "SAMX"[k]
                        for k in range(4)
                    )
                )
            ):
                count += 1
    return count


rot1 = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
rot2 = [[1, -1], [1, 1], [-1, 1], [-1, -1]]
rot3 = [[-1, -1], [1, -1], [1, 1], [-1, 1]]
rot4 = [[-1, 1], [-1, -1], [1, -1], [1, 1]]


def findCrossMas(grid, direction):
    count = 0
    len_x = len(grid)
    len_y = len(grid[0])
    for x in range(1, len_x - 1):
        for y in range(1, len_y - 1):
            if grid[x][y] == "A" and all(
                grid[x + direction[k][0]][y + direction[k][1]] == "MMSS"[k]
                for k in range(len("MMSS"))
            ):
                count += 1
    return count


print(
    f"Part1:  {findXmas(grid, horizontal)+findXmas(grid, vertical)+findXmas(grid, dia1)+findXmas(grid, dia2)}"
)
print(
    f"Part1:  {findCrossMas(grid, rot1)+findCrossMas(grid, rot2)+findCrossMas(grid, rot3)+findCrossMas(grid, rot4)}"
)

# %%
