# %%

with open("input.txt") as f:
    data = [[int(y) for y in x.split("-")] for x in f.readline().strip().split(",")]


# %% part1
def checkRepetition(num_int: int):
    num = str(num_int)
    return num[: len(num) // 2] == num[len(num) // 2 :]


result = sum(i for x, y in data for i in range(x, y + 1) if checkRepetition(i))
print(f"Part1: {result}")  # 54641809925


# %% part 2
def checkRepetitionMulti(num_int: int):
    num = str(num_int)
    for i in range(2, len(num) + 1):
        if len(num) % i != 0:
            continue
        l = len(num) // i
        if all(
            num[l * x : l * (x + 1)] == num[l * (x + 1) : l * (x + 2)]
            for x in range(i - 1)
        ):
            return True
    return False


result = sum(i for x, y in data for i in range(x, y + 1) if checkRepetitionMulti(i))
print(f"Part2: {result}")  # 73694270688

# %%
