#%%
import numpy as np

expense = np.genfromtxt("input.txt")


def search(array, l, h, res):
    while l < h and (s := array[l] + array[h]) != res:
        if s < res:
            l += 1
        else:
            h -= 1
    return l, h


# %% part 1
expense = np.sort(expense)

low, high = search(expense, 0, expense.shape[0] - 1, 2020)

print(
    f"Part 1 - Expenses: {expense[low]}*{expense[high]} = {expense[low]*expense[high]}"
)

# %% part 2

for pivot in range(expense.shape[0] - 1):
    low, high = search(expense, pivot + 1, expense.shape[0] - 1, 2020 - expense[pivot])

    if expense[low] + expense[high] + expense[pivot] == 2020:
        break

print(
    f"Part 2 - Expenses: {expense[pivot]}*{expense[low]}*{expense[high]} = {expense[pivot]*expense[low]*expense[high]}"
)

# %%
