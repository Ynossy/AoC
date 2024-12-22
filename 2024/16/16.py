# %%
from heapq import heapify, heappush, heappop 

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
nodes = []
heapify(nodes)
heappush(nodes, (0 ,([start], 0, 0)))  # (heap score, (path, direction, score))

PATH, D, S = 0, 1, 2

maze = [row.copy() for row in initial_maze]
maze[start[0]][start[1]] = 0

optimalSet = {start, end}
paths = []

while nodes:
    node = heappop(nodes)[1]
    if node[S] > maze[end[0]][end[1]]:
        break
    for i in [-1, 0, 1]:
        nd = (node[D] + i) % len(directions)
        nx = node[PATH][-1][0] + directions[nd][0]
        ny = node[PATH][-1][1] + directions[nd][1]
        nx2 = node[PATH][-1][0] + 2*directions[nd][0]
        ny2 = node[PATH][-1][1] + 2*directions[nd][1]
        dS = 1001 if i != 0 else 1
        if maze[nx][ny] != -1:
            if node[S] + dS <= maze[nx][ny] and node[S] + dS <= maze[end[0]][end[1]]:
                maze[nx][ny] = node[S] + dS
                if nx == end[0] and ny == end[1]:
                    paths.append((node[S] + dS, node[PATH]))
                else:
                    heappush(nodes, (node[S],(node[PATH]+[(nx, ny)], nd, node[S] + dS)))
            elif (maze[nx2][ny2] != -1 
                  and node[S] + dS + 1 <= maze[nx2][ny2] and node[S] + dS + 1 <= maze[end[0]][end[1]]):
                # edge case where we go straight over a node where already a turn occured
                if nx2 == end[0] and ny2 == end[1]:
                    paths.append((node[S]+ dS + 1, node[PATH]+[(nx, ny)]))
                else:
                    heappush(nodes, (node[S],(node[PATH]+[(nx, ny),(nx2, ny2)], nd, node[S] + dS + 1)))

print(f"Part 1: {maze[1][-2]}")

for p in paths:
    if p[0] != maze[1][-2]:
        continue
    for n in p[1]:
        optimalSet.add(n)

print(f"Part 2: {len(optimalSet)}")
# %%
