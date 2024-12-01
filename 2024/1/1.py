# %%
with open("input.txt") as f:
    numbers = [[int(y) for y in x.strip().split("   ")] for x in f.readlines()]

# %%
list1 = [x[0] for x in numbers]
list2 = [x[1] for x in numbers]

list1.sort()
list2.sort()

result = sum(abs(list1[i] - list2[i]) for i in range(len(list1)))

print(f"Result Part 1: {result}")
# %% Part 2

similarity = sum(x*list2.count(x) for x in list1)
print(f"Result 2: {similarity}")

# %%
