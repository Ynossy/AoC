# %%
test = False

file = "example.txt" if test else "input.txt"

with open(file) as f:
    cells = [[int(c.split(",")[0]), int(c.split(",")[1])] for c in f.readlines()]

# %%
size = 6 if test else 70
byte_count = 12 if test else 1024

memory = [[float("inf") for _ in range(size + 1)] for _ in range(size + 1)]

for i in range(byte_count):
    memory[cells[i][1]][cells[i][0]] = -1


nodes = [(0, 0)]
memory[0][0] = 0
end = (size, size)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

while nodes:
    current = nodes.pop()
    for d in directions:
        nx = current[0] + d[0]
        ny = current[1] + d[1]
        if not (0 <= nx <= size and 0 <= ny <= size) or memory[nx][ny] == -1:
            continue
        if memory[current[0]][current[1]] + 1 < memory[nx][ny]:
            memory[nx][ny] = memory[current[0]][current[1]] + 1
            nodes.append((nx, ny))

print(f"Part 1: {memory[end[0]][end[1]]}")
# %%
