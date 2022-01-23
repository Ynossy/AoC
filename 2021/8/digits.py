#%%
import numpy as np
from time import perf_counter

with open("input.txt") as f:
    lines = f.readlines()

digits = [x.split(" | ")[1] for x in lines]
digits = np.array([x.strip().split(" ") for x in digits])

# 1: 2seg 4: 4seg 7: 3seg  8: 7seg
l = np.char.str_len(digits)
amount = np.sum(l == 2) + np.sum(l == 4) + np.sum(l == 3) + np.sum(l == 7)
print(f"Digits 1,4,7 or 8 appear {amount} times")

#%% part2 Ugly shit but works

samples = [x.split(" | ")[0] for x in lines]
samples = np.array([x.strip().split(" ") for x in samples])

assignment = {17: 1, 34: 2, 39: 3, 30: 4, 37: 5, 41: 6, 25: 7, 49: 8, 45: 9, 42: 0}
start = perf_counter()
numbers = np.zeros(digits.shape)
for j in range(samples.shape[0]):
    # fill in number segments into 0/1 matrix
    segments = np.zeros((10, 7))
    for i, dig in enumerate(samples[j]):
        segments[i, :] = [x in dig for x in "abcdefg"]
    output_segments = np.zeros((4, 7))
    for i, dig in enumerate(digits[j]):
        output_segments[i, :] = [x in dig for x in "abcdefg"]

    # correlate all values and match them with precalculated scores
    correlation = np.sum(output_segments @ segments.T, axis=1)
    numbers[j, :] = [assignment[x] for x in correlation]

# convert from matrix to decimal sum
col_sum = np.sum(numbers, axis=0)
dec = col_sum[0] * 1000 + col_sum[1] * 100 + col_sum[2] * 10 + col_sum[3]
print(f"RunTime: {perf_counter()-start}")
print(f"Result: {dec}")
# %% precalculate correlation mapping

# segments = np.array([
#     [0,0,1,0,0,1,0],
#     [1,0,1,1,1,0,1],
#     [1,0,1,1,0,1,1],
#     [0,1,1,1,0,1,0],
#     [1,1,0,1,0,1,1],
#     [1,1,0,1,1,1,1],
#     [1,0,1,0,0,1,0],
#     [1,1,1,1,1,1,1],
#     [1,1,1,1,0,1,1],
#     [1,1,1,0,1,1,1],
# ])

# np.sum(segments@segments.T,axis=1) =
# [17, 34, 39, 30, 37, 41, 25, 49, 45, 42]
#  1   2   3   4   5   6   7   8   9   0

