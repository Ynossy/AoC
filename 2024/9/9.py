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
