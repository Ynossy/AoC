#%%
import numpy as np

with open("input.txt") as f:
    lines = f.readlines()

on = [int(x.split()[0] == "on") for x in lines]

coords = np.array(
    [
        [[int(x) for x in y[2:].split("..")] for y in z.split()[1].split(",")]
        for z in lines
    ]
)


# %% part 1:

cubes = np.zeros((101, 101, 101))

for i in range(20):
    cubes[
        coords[i, 0, 0] + 50 : coords[i, 0, 1] + 51,
        coords[i, 1, 0] + 50 : coords[i, 1, 1] + 51,
        coords[i, 2, 0] + 50 : coords[i, 2, 1] + 51,
    ] = on[i]

print(np.sum(cubes))
# %% forget part 2

