# %%
with open("input.txt") as f:
    data = f.read().strip().splitlines()
    maze_initial = []
    for i in range(len(data)):
        row = []
        for j in range(len(data[0])):
            if data[i][j] == "S":
                s = (i, j)
                row.append(float("inf"))
            elif data[i][j] == "E":
                e = (i, j)
                row.append(float("inf"))
            elif data[i][j] == ".":
                row.append(float("inf"))
            elif data[i][j] == "#":
                row.append(-1)
        maze_initial.append(row)

dFromStart = [r.copy() for r in maze_initial]
dFromEnd = [r.copy() for r in maze_initial]


def findLengths(maze, start):
    nodes = [start]
    maze[start[0]][start[1]] = 0
    while nodes:
        current = nodes.pop()
        for d in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx = current[0] + d[0]
            ny = current[1] + d[1]
            if maze[nx][ny] == -1:
                continue
            if maze[current[0]][current[1]] + 1 < maze[nx][ny]:
                maze[nx][ny] = maze[current[0]][current[1]] + 1
                nodes.append((nx, ny))


findLengths(dFromStart, s)
findLengths(dFromEnd, e)

nominal_length = dFromStart[e[0]][e[1]]


def countShortcuts(pico):
    shortcuts = [
        (i, j)
        for i in range(-pico, pico + 1)
        for j in range(-pico, pico + 1)
        if abs(i) + abs(j) <= pico
    ]
    res = 0
    for x in range(len(dFromStart)):
        for y in range(len(dFromStart[0])):
            if nominal_length - dFromStart[x][y] <= 100 or dFromStart[x][y] == -1:
                continue
            for cheat in shortcuts:
                nx = x + cheat[0]
                ny = y + cheat[1]
                if not (
                    0 <= nx < len(dFromStart)
                    and 0 <= ny < len(dFromStart[0])
                    and dFromEnd[nx][ny] != -1
                ):
                    continue

                cheat_advantage = nominal_length - (
                    dFromStart[x][y] + dFromEnd[nx][ny] + abs(cheat[0]) + abs(cheat[1])
                )
                if cheat_advantage >= 100:
                    res += 1
    return res


print(f"Part 1: {countShortcuts(2)}")
print(f"Part 2: {countShortcuts(20)}")
