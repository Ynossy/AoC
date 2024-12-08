#%%

with open("input.txt") as f:
    guard_map =  f.readlines()
    guard_map = [list(x.strip()) for x in guard_map]
    for x in range(len(guard_map)):
        for y in range(len(guard_map[x])):
            if guard_map[x][y] == '^':
                guard_map[x][y] = 'X'
                guard_start_position = (x,y)
                break
# %%

directions = [(-1,0), (0,1), (1,0), (0,-1)]
direction_idx = 0

guard_postion = guard_start_position
result = 1
while(True):
    new_x = guard_postion[0]+ directions[direction_idx][0]
    new_y = guard_postion[1]+ directions[direction_idx][1]
    if not (0<= new_x  < len(guard_map)
        and 0<= new_y < len(guard_map[0])):
        break
    
    if guard_map[new_x][new_y] == "#":
        direction_idx += 1
        direction_idx %= 4
    elif guard_map[new_x][new_y] == '.':
        guard_map[new_x][new_y] = "X"
        guard_postion = (new_x, new_y)
        result += 1
    elif guard_map[new_x][new_y] == 'X':
        guard_postion = (new_x, new_y)
    else:
        print(f"invalid character: {guard_map[new_x][new_y]}")
        break

print(f"Part 1: {result}")
# %%
