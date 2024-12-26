# %%
test = False

file = "example.txt" if test else "input.txt"

with open(file) as f:
    cells = [[int(c.split(",")[0]), int(c.split(",")[1])] for c in f.readlines()]

# %%
import heapq

size = 6 if test else 70
byte_count = 12 if test else 1024


def getShortestPath(bytes_n):
    memory = [[float("inf") for _ in range(size + 1)] for _ in range(size + 1)]

    for i in range(bytes_n):
        memory[cells[i][1]][cells[i][0]] = -1

    nodes = []
    heapq.heappush(nodes, (0, (0, 0)))
    memory[0][0] = 0
    end = (size, size)

    while nodes:
        current = heapq.heappop(nodes)[1]
        if current[0] == end[0] and current[1] == end[1]:
            break
        for d in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx = current[0] + d[0]
            ny = current[1] + d[1]
            if not (0 <= nx <= size and 0 <= ny <= size) or memory[nx][ny] == -1:
                continue
            if memory[current[0]][current[1]] + 1 < memory[nx][ny]:
                memory[nx][ny] = memory[current[0]][current[1]] + 1
                heapq.heappush(nodes, (memory[nx][ny], (nx, ny)))
    return memory[end[0]][end[1]]


print(f"Part 1: {getShortestPath(byte_count)}")

left = 0
right = len(cells)
while True:
    mid = (left + right) // 2
    pm = getShortestPath(mid)
    if pm == float("inf"):
        right = mid
    else:
        left = mid
    if right == left + 1:
        print(f"Part 2: {cells[right-1][0]},{cells[right-1][1]}")
        break
# %%
