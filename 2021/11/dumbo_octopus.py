#%%
import numpy as np
from io import StringIO

# task
input = """4472562264
8631517827
7232144146
2447163824
1235272671
5133527146
6511372417
3841841614
8621368782
3246336677"""

# # example
# input = """5483143223
# 2745854711
# 5264556173
# 6141336146
# 6357385478
# 4167524645
# 2176841721
# 6882881134
# 4846848554
# 5283751526"""

octos = np.genfromtxt(StringIO(input), delimiter=1)
max_y, max_x = octos.shape


def flash(map, y, x):
    if map[y, x] <= 9:
        return map

    map[y, x] = 0

    if x > 0:
        map = update(map, y, x - 1)

    if x < max_x - 1:
        map = update(map, y, x + 1)

    if y > 0:
        map = update(map, y - 1, x)
        if x > 0:
            map = update(map, y - 1, x - 1)
        if x < max_x - 1:
            map = update(map, y - 1, x + 1)

    if y < max_y - 1:
        map = update(map, y + 1, x)
        if x > 0:
            map = update(map, y + 1, x - 1)
        if x < max_x - 1:
            map = update(map, y + 1, x + 1)

    return map


def update(map, y, x):
    if map[y, x]:
        map[y, x] += 1
    if map[y, x] > 9:
        map = flash(map, y, x)
    return map


flash_count = 0
for i in range(1000):
    octos += 1
    for y, x in list(zip(*np.where(octos > 9))):
        octos = flash(octos, y, x)
    if i < 100:
        flash_count += np.sum(octos == 0)
    if np.sum(octos == 0) == max_y * max_x:
        print(f"All Flashed at t={i+1}")
        break

print(f"{flash_count} flashed were made until timestep 100")
