# %%
max_x = 11
max_y = 7
file = "example.txt"

max_x = 101
max_y = 103
file = "input.txt"

with open(file) as f:
    data = f.readlines()
    robots = []
    for l in data:
        p, v = l.strip().split(" ")
        p = [int(x) for x in p[2:].split(",")]
        v = [int(x) for x in v[2:].split(",")]
        robots.append([p, v])
# %%

time = 100


def moveRobots(time):
    return [
        [
            (robot[0][0] + time * robot[1][0]) % max_x,
            (robot[0][1] + time * robot[1][1]) % max_y,
        ]
        for robot in robots
    ]


robots_moved = moveRobots(100)
quadrants = [0, 0, 0, 0]
for robot in robots_moved:
    if robot[0] < max_x // 2:
        if robot[1] < max_y // 2:
            quadrants[0] += 1
        elif max_y // 2 < robot[1]:
            quadrants[2] += 1
    elif max_x // 2 < robot[0]:
        if robot[1] < max_y // 2:
            quadrants[1] += 1
        elif max_y // 2 < robot[1]:
            quadrants[3] += 1

res = quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]
print(f"Part 1: {res}")

# %%
import numpy as np


def printRobots(robots_):
    grid = [[0 for _ in range(max_y)] for _ in range(max_x)]
    for robot in robots_:
        grid[robot[0]][robot[1]] += 1
    for i in range(max_x):
        for j in range(max_y):
            print("." if grid[i][j] == 0 else grid[i][j], end=" ")
        print("")


std_min = 1e10
idx = 0
for i in range(10000):
    robots_moved = np.array(moveRobots(i))
    s_new = np.std(np.sum(robots_moved, axis=1))
    if s_new < std_min:
        std_min = s_new
        idx = i

print(f"Part 2: {idx}")
robots_moved = moveRobots(idx)
printRobots(robots_moved)

# %%
