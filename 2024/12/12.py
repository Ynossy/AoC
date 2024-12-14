# %%

with open("input.txt") as f:
    plants = [list(x.strip()) for x in f.readlines()]
# %%

dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

"""
Corners for # are either 
##      #O
#O  or  O  in all 4 directions 
"""
cornersDir = [
    [[0, 1], [1, 0], [1, 1]],
    [[0, 1], [-1, 0], [-1, 1]],
    [[0, -1], [1, 0], [1, -1]],
    [[0, -1], [-1, 0], [-1, -1]],
]


def inRange(x, y):
    return 0 <= x < len(plants) and 0 <= y < len(plants[0])


visited = [[False for _ in row] for row in plants]
res1 = 0
res2 = 0
for i in range(len(plants)):
    for j in range(len(plants[i])):
        if visited[i][j]:
            continue
        plant = plants[i][j]
        flood = [(i, j)]
        visited[i][j] = True
        area = 1
        perimeter = 0
        corners = 0
        while flood:
            cur = flood.pop()
            for d in dirs:
                nx = d[0] + cur[0]
                ny = d[1] + cur[1]
                if not inRange(nx, ny):
                    perimeter += 1
                elif plants[nx][ny] == plant:
                    if not visited[nx][ny]:
                        area += 1
                        flood.append((nx, ny))
                        visited[nx][ny] = True
                else:
                    perimeter += 1
            for c in cornersDir:
                checks = []
                for p in c:
                    nx = cur[0] + p[0]
                    ny = cur[1] + p[1]
                    checks.append(inRange(nx, ny) and plants[nx][ny] == plant)
                if not (checks[0] or checks[1]) or (
                    checks[0] and checks[1] and not checks[2]
                ):
                    corners += 1
        res1 += area * perimeter
        res2 += area * corners
print(f"Part 1: {res1}, Part2: {res2}")

# %%
