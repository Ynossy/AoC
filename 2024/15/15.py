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


def printMap(warehouse, position):
    for i in range(len(warehouse)):
        for j in range(len(warehouse[i])):
            if i == position[0] and j == position[1]:
                print("@", end="")
            else:
                print(warehouse[i][j], end="")
        print("")


pos = start_position
for move in moves:
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

map_extended = []
for i in range(len(warehouse_initial)):
    row = []
    for j in range(len(warehouse_initial[i])):
        cur = warehouse_initial[i][j]
        if cur == ".":
            row += [".", "."]
        elif cur == "#":
            row += ["#", "#"]
        elif cur == "O":
            row += ["[", "]"]
    map_extended.append(row)

p2_start = [start_position[0], start_position[1] * 2]


def isPushable(pos, d):
    if d[0] == 0:
        if map_extended[pos[0]][pos[1]] in ["[", "]"]:
            return isPushable([pos[0], pos[1] + 2 * d[1]], d)
        elif map_extended[pos[0]][pos[1]] == "#":
            return False
        elif map_extended[pos[0]][pos[1]] == ".":
            return True
    else:
        if map_extended[pos[0]][pos[1]] == ".":
            return True
        elif map_extended[pos[0]][pos[1]] == "#":
            return False
        elif map_extended[pos[0]][pos[1]] in ["[", "]"]:
            dy = 1 if map_extended[pos[0]][pos[1]] == "[" else -1
            nx = pos[0] + d[0]
            ny = pos[1]
            return isPushable([nx, ny], d) and isPushable([nx, ny + dy], d)


def pushBox(pos, d):
    if map_extended[pos[0]][pos[1]] in [".", "#"]:
        return
    if d[0] == 0:
        nx = pos[0]
        ny = pos[1] + 2 * d[1]
        if map_extended[nx][ny] in ["[", "]"]:
            pushBox([nx, ny], d)

        map_extended[nx][ny] = map_extended[pos[0]][pos[1] + d[1]]
        map_extended[pos[0]][pos[1] + d[1]] = map_extended[pos[0]][pos[1]]
        map_extended[pos[0]][pos[1]] = "."
    else:
        nx = pos[0] + d[0]
        ny = pos[1]
        dy = 1 if map_extended[pos[0]][pos[1]] == "[" else -1
        pushBox([nx, ny], d)
        pushBox([nx, ny + dy], d)
        map_extended[nx][pos[1] + dy] = map_extended[pos[0]][pos[1] + dy]
        map_extended[pos[0]][pos[1] + dy] = "."

        map_extended[nx][pos[1]] = map_extended[pos[0]][pos[1]]
        map_extended[pos[0]][pos[1]] = "."


pos = p2_start
for move in moves:
    d = directions[move]
    nextPos = [pos[0] + d[0], pos[1] + d[1]]
    if map_extended[nextPos[0]][nextPos[1]] == ".":
        pos = nextPos
    elif isPushable(nextPos, d):
        pushBox(nextPos, d)
        pos = nextPos

res = 0
for i in range(len(map_extended)):
    for j in range(len(map_extended[i])):
        if map_extended[i][j] == "[":
            res += 100 * i + j

print(f"Part 2: {res}")

# %%
