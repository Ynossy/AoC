# %%

with open("input.txt") as f:
    initial_stones = [int(x) for x in f.read().strip().split(" ")]

# %%

stones = {x: 1 for x in initial_stones}
stones_temp = {}


def insertStone(stone, amount):
    if stone in stones_temp:
        stones_temp[stone] = stones_temp[stone] + amount
    else:
        stones_temp[stone] = amount


for i in range(75):
    stones_temp = {}
    for s in stones:
        if s == 0:
            insertStone(1, stones[s])
        else:
            s_str = str(s)
            if len(s_str) % 2 == 0:
                insertStone(int(s_str[len(s_str) // 2 :]), stones[s])
                insertStone(int(s_str[: len(s_str) // 2]), stones[s])
            else:
                insertStone(s * 2024, stones[s])
    stones = stones_temp.copy()
    if i == 24:
        print(f"Part 1: {sum(stones[x] for x in stones)}")
    elif i == 74:
        print(f"Part 2: {sum(stones[x] for x in stones)}")


# %%
