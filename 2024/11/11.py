#%%

with open("input.txt") as f:
    initial_stones = [int(x) for x in f.read().strip().split(" ")]

#%%

stones = initial_stones.copy()
for i in range(25):
    stones_temp = []
    for s in stones:
        if s == 0:
            stones_temp.append(1)
        else:
            s_str = str(s)
            if len(s_str)%2 == 0:
                stones_temp.append(int(s_str[len(s_str)//2:]))
                stones_temp.append(int(s_str[:len(s_str)//2]))
            else:
                stones_temp.append(s*2024)
    stones = stones_temp
    print(f"{i}-{len(stones)}")
            

# %%
