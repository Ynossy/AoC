#%%
import numpy as np
from time import perf_counter

start = perf_counter()

values = {".": 0, ">": 1, "v": 2}
# with open("example.txt") as f:
with open("input.txt") as f:
    cucumbers = np.array([[values[c] for c in line.strip()] for line in f])

# move right
def move(cucumbers, char, axis):
    moved_cu = values[char] * (cucumbers == values[char])
    moved_mask = np.roll(moved_cu, 1, axis) * (cucumbers == 0)
    cucumbers += moved_mask - np.roll(moved_mask, -1, axis)
    return cucumbers, np.sum(moved_mask)


step = 0
moving = 1
while moving:
    step += 1
    cucumbers, movingR = move(cucumbers, ">", 1)
    cucumbers, movingD = move(cucumbers, "v", 0)
    moving = movingR + movingD
print(f"Stopped after {step} steps")

print(f"RunTime: {perf_counter() - start}")

# %%
