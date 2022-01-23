#%%
import numpy as np
import pandas as pd

with open("input.txt") as f:
    lines = f.readlines()

# lines = ["00100"
# ,"11110"
# ,"10110"
# ,"10111"
# ,"10101"
# ,"01111"
# ,"00111"
# ,"11100"
# ,"10000"
# ,"11001"
# ,"00010"
# ,"01010"]

# convert to char array
binary = np.array([list(x.strip()) for x in lines])
# convert to integer array
binary = binary.astype(int)
# find most common value (1 or 0)
gamma = np.round(np.average(binary, axis=0))
# back to string list
gamma = list(gamma.astype(int).astype(str))
# join to number
gamma = int("".join(gamma), 2)

# invert for second value
# epsilon = gamma ^ int("11111",2) #example
epsilon = gamma ^ int("111111111111", 2)

print(f"Result 1 is {gamma}*{epsilon}={gamma*epsilon}")

#%% part 2
binary = np.array([list(x.strip()) for x in lines])
binary = binary.astype(int)

oxygen = binary
for i in range(binary.shape[1]):
    pivot = np.average(oxygen[:, i])
    pivot = 1 if pivot >= 0.5 else 0  # python, why?
    oxygen = oxygen[oxygen[:, i] == pivot]
    if oxygen.shape[0] == 1:
        print(f"remaining Number: {oxygen}")
        break

oxygen = list(oxygen[0].astype(int).astype(str))
oxygen = int("".join(oxygen), 2)

co2 = binary
for i in range(binary.shape[1]):
    pivot = np.average(co2[:, i])
    pivot = 0 if pivot >= 0.5 else 1
    co2 = co2[co2[:, i] == pivot]
    if co2.shape[0] == 1:
        print(f"remaining Number: {co2}")
        break
co2 = list(co2[0].astype(int).astype(str))
co2 = int("".join(co2), 2)

print(f"2. Result: {oxygen}*{co2}={oxygen*co2}")

# %%
