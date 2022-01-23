#%%
import numpy as np
from io import StringIO

example = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

# map = np.genfromtxt(StringIO(example), delimiter=1)
map = np.genfromtxt("input.txt", delimiter=1)
# %%
import heapq
from time import perf_counter


def path_search(map):
    start = perf_counter()

    points = []
    heapq.heappush(points, (0, (0, 0)))
    risk_map = np.full(map.shape, np.inf)
    risk_map[0, 0] = 0

    while points:
        px, py = heapq.heappop(points)[1]
        for pxi, pyi in [(px + 1, py), (px - 1, py), (px, py + 1), (px, py - 1)]:
            if (
                map.shape[0] > pxi >= 0
                and map.shape[1] > pyi >= 0
                and risk_map[pxi, pyi] > risk_map[px, py] + map[pxi, pyi]
            ):
                risk_map[pxi, pyi] = risk_map[px, py] + map[pxi, pyi]
                heapq.heappush(points, (risk_map[pxi, pyi], (pxi, pyi)))

    print(f"RunTime: {perf_counter()-start}")
    print(f"Total Risk to bottom left: {risk_map[-1,-1]}")


# %%

# part 1:
path_search(map)

# part 2:
increment = np.array(
    [
        [0, 1, 2, 3, 4],
        [1, 2, 3, 4, 5],
        [2, 3, 4, 5, 6],
        [3, 4, 5, 6, 7],
        [4, 5, 6, 7, 8],
    ]
)
map_extended = np.tile(map, [5, 5]) + np.kron(increment, np.ones(map.shape))
map_extended = (map_extended - 1) % 9 + 1

path_search(map_extended)
# %%
