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
                x + direction[-1][0] >= len_x
                or x + direction[-1][0] < 0
                or y + direction[-1][1] >= len_y
                or y + direction[-1][1] < 0
            ):
                continue
            if (
                grid[x + direction[0][0]][y + direction[0][1]] in "X"
                and grid[x + direction[1][0]][y + direction[1][1]] in "M"
                and grid[x + direction[2][0]][y + direction[2][1]] in "A"
                and grid[x + direction[3][0]][y + direction[3][1]] in "S"
            ) or (
                grid[x + direction[0][0]][y + direction[0][1]] in "S"
                and grid[x + direction[1][0]][y + direction[1][1]] in "A"
                and grid[x + direction[2][0]][y + direction[2][1]] in "M"
                and grid[x + direction[3][0]][y + direction[3][1]] in "X"
            ):
                count += 1
    return count


print(
    f"Part1:  {findXmas(grid, horizontal)+findXmas(grid, vertical)+findXmas(grid, dia1)+findXmas(grid, dia2)}"
)

# %%
