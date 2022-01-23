#%%
import numpy as np

# with open("input.txt") as f:
#     lines = f.readlines()

data = np.genfromtxt("input.txt")

# verification
example = np.array([199, 200, 208, 210, 200, 207, 240, 269, 260, 263])
# print(np.sum(np.diff(example)>0))

print(f"larger are {np.sum(np.diff(data)>0)} measurements")
#%% sliding window
window = np.array([1, 1, 1])

# sliding3_ex = np.convolve(example, window, mode='valid')
# print(np.sum(np.diff(sliding3_ex)>0))

sliding3 = np.convolve(data, window, mode="valid")
print(f"Sliding Window: Larger are {np.sum(np.diff(sliding3)>0)} measurements")
# %%
