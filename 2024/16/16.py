# %%


def parseChar(c):
    return float("inf") if c in "S.E" else -1


with open("input.txt") as f:
    data = f.readlines()
    initial_maze = [[parseChar(c) for c in y.strip()] for y in data]
    start = (len(initial_maze) - 2, 1)
    end = (1, len(initial_maze[0]) - 2)
    assert data[start[0]][start[1]] == "S"
    assert data[end[0]][end[1]] == "E"

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# %%

nodes = [start + (0, 0)]  # (x, y, direction, score)

X, Y, D, S = 0, 1, 2, 3

maze = [row.copy() for row in initial_maze]
maze[start[X]][start[Y]] = 0

while nodes:
    node = nodes.pop()
    # move forward
    for i in [-1, 0, 1]:
        nd = (node[D] + i) % len(directions)
        nx = node[X] + directions[nd][X]
        ny = node[Y] + directions[nd][Y]
        dS = 1001 if i != 0 else 1
        if maze[nx][ny] != -1 and node[S] + dS < maze[nx][ny]:
            maze[nx][ny] = node[S] + dS
            nodes.append((nx, ny, nd, node[S] + dS))

print(f"Part 1: {maze[1][-2]}")

# %%
