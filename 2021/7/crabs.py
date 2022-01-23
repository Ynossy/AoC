#%%
import numpy as np

# input = np.array([16,1,2,0,4,2,7,1,2,14])
input = np.genfromtxt("input.txt", delimiter=",", dtype=int)

#%% part 1 - solution is the median
pivot = np.median(input)
result = np.sum(np.abs(input - pivot))

print(f"Best position at {pivot} with {result} fuel needed")

#%% part 2 - guess the mean (exact for continous numbers) and search a few numbers around it
pivot_guess = int(np.mean(input) + 0.5)
pivots = np.arange(pivot_guess - 5, pivot_guess + 5)

costs = np.cumsum(np.arange(max(input)))
results = [np.sum(costs[np.abs(input - x)]) for x in pivots]

print(
    f"Best position at {pivots[np.argmin(results)]} with {np.min(results)} fuel needed"
)
