# %%
with open("input.txt") as f:
    warehouse_initial, moves = f.read().strip().split("\n\n")
    warehouse_initial = [list(row) for row in warehouse_initial.strip().split("\n")]
    for i in range(len(warehouse_initial)):
        for j in range(len(warehouse_initial[i])):
            if warehouse_initial[i][j] == "@":
                warehouse_initial[i][j] = "."
                start_position = [i, j]
    moves = moves.replace("\n", "")
# %%

directions = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}
warehouse = [x.copy() for x in warehouse_initial]


def printMap(position):
    for i in range(len(warehouse)):
        for j in range(len(warehouse[i])):
            if i == position[0] and j == position[1]:
                print("@", end="")
            else:
                print(warehouse[i][j], end="")
        print("")


pos = start_position
for move in moves:
    # printMap(pos)
    # print(f"Move: {move}")
    d = directions[move]
    inFront = warehouse[pos[0] + d[0]][pos[1] + d[1]]
    if inFront == ".":
        pos = (pos[0] + d[0], pos[1] + d[1])
        continue
    elif inFront == "#":
        continue
    else:
        di = 1
        while warehouse[pos[0] + di * d[0]][pos[1] + di * d[1]] not in ["#", "."]:
            di += 1
        if di == 1 or warehouse[pos[0] + di * d[0]][pos[1] + di * d[1]] == "#":
            continue

    for i in range(1, di):
        p1x = pos[0] + (di - i + 1) * d[0]
        p1y = pos[1] + (di - i + 1) * d[1]

        p2x = pos[0] + (di - i) * d[0]
        p2y = pos[1] + (di - i) * d[1]
        warehouse[p1x][p1y], warehouse[p2x][p2y] = (
            warehouse[p2x][p2y],
            warehouse[p1x][p1y],
        )
    pos = (pos[0] + d[0], pos[1] + d[1])

res = 0
for i in range(len(warehouse)):
    for j in range(len(warehouse[i])):
        if warehouse[i][j] == "O":
            res += 100 * i + j

print(f"Part 1: {res}")
# %%
