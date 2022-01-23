#%%
import numpy as np
from io import StringIO

heigth_map = np.genfromtxt("input.txt", delimiter=1)
# ex = """2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678"""
# heigth_map = np.genfromtxt(StringIO(ex), delimiter=1)

#%% Find Low Points
# Just shift all values in each direction for easy comparison
up = np.concatenate([heigth_map[1:, :], 10 * np.ones((1, heigth_map.shape[1]))])
down = np.concatenate([10 * np.ones((1, heigth_map.shape[1])), heigth_map[:-1, :]])
left = np.concatenate(
    [heigth_map[:, 1:], 10 * np.ones((heigth_map.shape[0], 1))], axis=1
)
right = np.concatenate(
    [10 * np.ones((heigth_map.shape[0], 1)), heigth_map[:, :-1]], axis=1
)

# branchless magic
score = (
    (heigth_map < up).astype(int)
    + (heigth_map < down).astype(int)
    + (heigth_map < left).astype(int)
    + (heigth_map < right).astype(int)
)

print(f"The Final sum is {np.sum(heigth_map[score==4]+1)}")

#%% Get basin size of each Low Point

# Classic Recursion
def add_neighbors(map, visited, y, x, counter):
    if map[y, x] == 9 or visited[y, x] == 1:
        return counter
    visited[y, x] = 1
    if x > 0:
        counter = add_neighbors(map, visited, y, x - 1, counter)
    if x < map.shape[1] - 1:
        counter = add_neighbors(map, visited, y, x + 1, counter)
    if y > 0:
        counter = add_neighbors(map, visited, y - 1, x, counter)
    if y < map.shape[0] - 1:
        counter = add_neighbors(map, visited, y + 1, x, counter)

    return counter + 1


my, mx = np.where(score == 4)
basin_size = np.zeros(my.shape)

for i, (y, x) in enumerate(zip(my, mx)):
    visited = np.zeros(heigth_map.shape)
    basin_size[i] = add_neighbors(heigth_map, visited, y, x, 0)

big3 = np.sort(basin_size)[-3:]
print(f"Biggest three basins: {big3} with product: {np.prod(big3)}")

# %%
