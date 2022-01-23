#%%
import numpy as np
import re

# data = np.genfromtxt("input.txt",delimiter=",",invalid_raise=False, dtype=int)

with open("input.txt") as f:
    lines = f.read().splitlines()
seperator = lines.index("")

instructions = lines[seperator + 1 :]
instructions = [re.split(" |=", x)[2:] for x in instructions]

data = np.array([x.split(",") for x in lines[0:seperator]], dtype=int)
sx, sy = np.max(data,axis=0)+1
transparent = np.zeros((sy,sx))
transparent[data[:, 1], data[:, 0]] = 1

#first step

if instructions[0][0] == 'x':
    pivot = int(instructions[0][1])
    transparent[:,:pivot] += np.fliplr(transparent[:,pivot+1:sx])
    sx = pivot
    print(f"Marks Count= {np.count_nonzero(transparent[:,:sx])}")

#%% second part
import matplotlib.pyplot as plt
from time import perf_counter

start = perf_counter()
sx, sy = np.max(data,axis=0)+1
transparent = np.zeros((sy,sx))
transparent[data[:, 1], data[:, 0]] = 1

for dir, inst in instructions:
    pivot = int(inst)
    if dir == 'x':
        transparent[:,:pivot] += np.fliplr(transparent[:,pivot+1:sx])
        sx = pivot
    else:
        transparent[:pivot,:] += np.flipud(transparent[pivot+1:sy,:])
        sy = pivot

result = transparent[:sy,:sx]
result[result>0] = 1
print(f"Runtime: {perf_counter()-start}")
plt.matshow(result)
