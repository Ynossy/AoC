# %%

with open("input.txt") as f:
    plants = [list(x.strip()) for x in f.readlines()]
# %%

dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

"""
Corners are either 
##      #O
#O  or  OO in all 4 directions 
"""
cornersDir = [
    [[0,1],[1,0],[1,1]],
    [[0,1],[-1,0],[-1,1]],
    [[0,-1],[1,0],[1,-1]],
    [[0,-1],[-1,0],[-1,-1]],
]

def inRange(x,y):
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
                if not inRange(nx,ny):
                    perimeter += 1
                elif plants[nx][ny] == plant:
                    if not visited[nx][ny]:
                        area += 1
                        flood.append((nx, ny))
                        visited[nx][ny] = True
                else:
                    perimeter += 1
            for c in cornersDir:
                n1x = cur[0] + c[0][0]
                n1y = cur[1] + c[0][1]
                n2x = cur[0] + c[1][0]
                n2y = cur[1] + c[1][1]
                n3x = cur[0] + c[2][0]
                n3y = cur[1] + c[2][1]
                n1Same = inRange(n1x, n1y) and plants[n1x][n1y] == plant
                n2Same = inRange(n2x, n2y) and plants[n2x][n2y] == plant
                n3Same = inRange(n3x, n3y) and plants[n3x][n3y] == plant

                if not (n1Same or n2Same) or (n1Same and n2Same and not n3Same):
                    corners += 1
        # print(f"Plant: {plant}, area: {area}, perimeter {perimeter}, corners: {corners}")
        res1 += area * perimeter
        res2 += area * corners
print(f"Part 1: {res1}, Part2: {res2}")

#p2: 865044 too low
# 872382 right

# %%
