# %%


def parse_map():
    with open("input.txt") as f:
        guard_map = f.readlines()
        guard_map = [list(x.strip()) for x in guard_map]
        for x in range(len(guard_map)):
            for y in range(len(guard_map[x])):
                if guard_map[x][y] == "^":
                    guard_map[x][y] = "X"
                    guard_start_position = (x, y)
                    break
    return guard_map, guard_start_position


# %%

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
direction_idx = 0

guard_map, guard_postion = parse_map()
result = 1
while True:
    new_x = guard_postion[0] + directions[direction_idx][0]
    new_y = guard_postion[1] + directions[direction_idx][1]
    if not (0 <= new_x < len(guard_map) and 0 <= new_y < len(guard_map[0])):
        break

    if guard_map[new_x][new_y] == "#":
        direction_idx += 1
        direction_idx %= 4
    elif guard_map[new_x][new_y] == ".":
        guard_map[new_x][new_y] = "X"
        guard_postion = (new_x, new_y)
        result += 1
    elif guard_map[new_x][new_y] == "X":
        guard_postion = (new_x, new_y)
    else:
        print(f"invalid character: {guard_map[new_x][new_y]}")
        break

print(f"Part 1: {result}")
# %%
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
directions_label = ["^", ">", "v", "<"]
direction_idx = 0

guard_map, guard_postion = parse_map()
guard_map[guard_postion[0]][guard_postion[1]] = "X"

loop_obstacle = set()


def checkLoop(initial_map, position, _direction_idx):
    map_copy = [x.copy() for x in initial_map]
    loop = False
    while True:
        new_x = position[0] + directions[_direction_idx][0]
        new_y = position[1] + directions[_direction_idx][1]
        if not (0 <= new_x < len(map_copy) and 0 <= new_y < len(map_copy[0])):
            break

        if map_copy[new_x][new_y] == "#":
            _direction_idx += 1
            _direction_idx %= 4
        elif map_copy[new_x][new_y] == ".":
            map_copy[new_x][new_y] = directions_label[_direction_idx]
            position = (new_x, new_y)
        else:
            if directions_label[_direction_idx] not in map_copy[new_x][new_y]:
                map_copy[new_x][new_y] += directions_label[_direction_idx]
            else:
                loop = True
                break
            position = (new_x, new_y)

    return loop


while True:
    new_x = guard_postion[0] + directions[direction_idx][0]
    new_y = guard_postion[1] + directions[direction_idx][1]
    if not (0 <= new_x < len(guard_map) and 0 <= new_y < len(guard_map[0])):
        break

    if guard_map[new_x][new_y] == ".": # can only place where i havent been yet
        guard_map[new_x][new_y] = "#"
        if checkLoop(guard_map, guard_postion, direction_idx):
            loop_obstacle.add((new_x, new_y))
        guard_map[new_x][new_y] = "."

    if guard_map[new_x][new_y] == "#":
        direction_idx += 1
        direction_idx %= 4
    elif guard_map[new_x][new_y] == ".":
        guard_map[new_x][new_y] = "X"
        guard_postion = (new_x, new_y)
        result += 1
    elif guard_map[new_x][new_y] == "X":
        guard_postion = (new_x, new_y)
    else:
        print(f"invalid character: {guard_map[new_x][new_y]}")
        break

print(f"Part 2: {len(loop_obstacle)}")  # 1023, 1033 too low | 2151 too high
# 1919 right (github)
# %%
