# %%

with open("input.txt") as f:
    plants = [list(x.strip()) for x in f.readlines()]
# %%

dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
visited = [[False for _ in row] for row in plants]
res = 0
for i in range(len(plants)):
    for j in range(len(plants[i])):
        if visited[i][j]:
            continue
        plant = plants[i][j]
        flood = [(i, j)]
        visited[i][j] = True
        area = 1
        perimeter = 0
        while flood:
            cur = flood.pop()
            for d in dirs:
                nx = d[0] + cur[0]
                ny = d[1] + cur[1]
                if not (0 <= nx < len(plants) and 0 <= ny < len(plants[0])):
                    perimeter += 1
                elif plants[nx][ny] == plant:
                    if not visited[nx][ny]:
                        area += 1
                        flood.append((nx, ny))
                        visited[nx][ny] = True
                else:
                    perimeter += 1
        # print(f"Plant: {plant}, area: {area}, perimeter {perimeter}")
        res += area * perimeter
print(f"Part 1: {res}")

# %%
