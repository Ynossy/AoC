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
print(f"Nominal path length: {nominal_length}")

shortcuts = [  # possible endpoints for cheating
    (2, 0, 1),
    (-2, 0, 1),
    (0, 2, 1),
    (0, -2, 1),
    (1, 1, 2),
    (1, -1, 2),
    (-1, -1, 2),
    (-1, 1 - 2),
]

res = 0
cheats = {}
for x in range(len(dFromStart)):
    for y in range(len(dFromStart[0])):
        for cheat in shortcuts:
            nx = x + cheat[0]
            ny = y + cheat[1]
            if not (
                0 <= nx < len(dFromStart)
                and 0 <= ny < len(dFromStart[0])
                and dFromEnd[nx][ny] != -1
                and dFromStart[x][y] != -1
            ):
                continue

            cheat_advantage = nominal_length - (dFromStart[x][y] + dFromEnd[nx][ny] + 2)
            if cheat_advantage > 0:
                if cheat_advantage in cheats:
                    cheats[cheat_advantage] += cheat[2]
                else:
                    cheats[cheat_advantage] = cheat[2]
            if cheat_advantage >= 100:
                res += 1

print(f"Part 1: {res}")
