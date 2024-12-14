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

# robots_moved = []
# for robot in robots:
#     nx = (robot[0][0] + time * robot[1][0]) % max_x
#     ny = (robot[0][1] + time * robot[1][1]) % max_y
#     # print(nx, ny)
#     robots_moved.append((nx,ny))
robots_moved = [
    [
        (robot[0][0] + 100 * robot[1][0]) % max_x,
        (robot[0][1] + 100 * robot[1][1]) % max_y,
    ]
    for robot in robots
]

quadrants =[0,0,0,0]
for robot in robots_moved:
    if robot[0] < max_x // 2:
        if robot[1] < max_y//2:
            quadrants[0] += 1
        elif max_y//2 < robot[1]:
            quadrants[2] += 1
    elif max_x//2 < robot[0]:
        if robot[1] < max_y//2:
            quadrants[1] += 1
        elif max_y//2 < robot[1]:
            quadrants[3] += 1

res = quadrants[0]*quadrants[1]*quadrants[2]*quadrants[3]
print(f"Part 1: {res}")

# %%
