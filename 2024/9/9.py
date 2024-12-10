#%%

with open("input.txt") as f:
    data = [int(c) for c in f.read().strip()]
    # files = data[::2]
    # spaces = data[1::2]
# %%

right_idx = len(data)-1
left_idx = 0
block = 0

file_id_left = 0
file_id_right = len(data)//2 + 1
right_file_remain = 0

result = 0
while left_idx <= right_idx:
    if left_idx%2 == 0:
        # file not moved
        for _ in range(data[left_idx]):
            result += file_id_left*block
            # print(file_id_left, end="")
            block += 1
        file_id_left += 1
    else:
        #space to fill
        space_len = data[left_idx]
        while space_len > 0:
            if right_file_remain == 0:
                right_file_remain = data[right_idx]
                right_idx -= 2
                file_id_right -= 1
            result += file_id_right*block
            # print(file_id_right, end="")
            right_file_remain -= 1
            block += 1
            space_len -= 1
            
    left_idx += 1
for _ in range(right_file_remain):
    # print(file_id_right, end="")
    result += file_id_right*block
    block +=1
print("")
print(f"Part 1: {result}") 
# 6'281'129'828'621 too high
# 6'279'058'075'753
# %%


ISSPACE = 0
LENGTH = 1
FILE_ID = 2

file_id_right = len(data)//2

filesystem = [[i%2!=0, x, i//2 if i%2==0 else -1] for i, x in enumerate(data)]

while file_id_right >= 0:
    file_idx_to_move = None
    for i in range(len(filesystem)):
        if filesystem[i][FILE_ID] == file_id_right:
            file_idx_to_move = i
            break
    for i in range(file_idx_to_move):
        if filesystem[i][ISSPACE] and (filesystem[i][LENGTH] >= filesystem[file_idx_to_move][LENGTH]):
            filesystem[i][LENGTH] -= filesystem[file_idx_to_move][LENGTH]
            temp = filesystem[file_idx_to_move].copy()
            filesystem[file_idx_to_move][ISSPACE] = True
            filesystem[file_idx_to_move][FILE_ID] = -1
            filesystem.insert(i, temp)
            break
    file_id_right -= 1
block = 0
result = 0
for f in filesystem:
    for _ in range(f[LENGTH]):
        if not f[ISSPACE]:
            result += block*f[FILE_ID]
        block += 1

print(f"Part 2: {result}") # takes 18 seconds, but works

# %%
