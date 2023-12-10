import numpy as np
from heapq import heapify, heappush, heappop
import time as time


def bfs(time_map, start, end, t0=0, forward=True):
    dim_x, dim_y = time_map[0].shape
    visited = np.zeros(time_map.shape)
    stack = [(None, start, t0)] if forward else [(None, end, t0)]
    dirs = [(0, 0, 1), (1, 0, 1), (-1, 0, 1), (0, 1, 1), (0, -1, 1)]
    while stack:
        state = stack.pop(0)
        # print(state[2])
        # finished
        if forward and state[0] == dim_x - 1 and state[1] == end:
            # print(f"Finished with {state}: pathlen: {state[2]+1}")
            return state[2] + 1
        if not forward and state[0] == 0 and state[1] == start:
            # print(f"Finished with {state}: pathlen: {state[2]+1}")
            return state[2] + 1
        # enter maze
        if state[0] is None:
            stack.append((None, state[1], state[2] + 1))
            if forward and time_map[state[2], 0, state[1]] == 0:
                stack.append((0, state[1], state[2] + 1))
            elif not forward and time_map[state[2], dim_x - 1, state[1]] == 0:
                stack.append((dim_x - 1, state[1], state[2] + 1))
            continue
        # actions
        for d in dirs:
            if (
                0 <= state[0] + d[0] < dim_x
                and 0 <= state[1] + d[1] < dim_y
                and time_map[state[2] + d[2], state[0] + d[0], state[1] + d[1]] == 0
                and visited[state[2] + d[2], state[0] + d[0], state[1] + d[1]] == False
            ):
                visited[state[2] + d[2], state[0] + d[0], state[1] + d[1]] = True
                stack.append((state[0] + d[0], state[1] + d[1], state[2] + d[2]))


def main():
    bench_t0 = time.time()
    with open("input.txt") as f:
        lines = f.read().strip().split("\n")
    raw_blizzards = [l[1:-1] for l in lines[1:-1]]
    start = lines[0].index(".") - 1
    end = lines[-1].index(".") - 1

    dim_x = len(raw_blizzards)
    dim_y = len(raw_blizzards[0])
    blizzards = np.zeros((4, dim_x, dim_y))
    idx = {"<": 0, ">": 1, "^": 2, "v": 3}
    for x in range(dim_x):
        for y in range(dim_y):
            if raw_blizzards[x][y] == ".":
                continue
            blizzards[idx[raw_blizzards[x][y]], x, y] = 1
    max_t = 2000
    time_map = np.zeros((max_t, dim_x, dim_y))
    for t in range(max_t):
        time_map[t] = np.sum(blizzards, axis=0)
        blizzards[0] = np.roll(blizzards[0], -1, axis=1)
        blizzards[1] = np.roll(blizzards[1], 1, axis=1)
        blizzards[2] = np.roll(blizzards[2], -1, axis=0)
        blizzards[3] = np.roll(blizzards[3], 1, axis=0)
    bench_t1 = time.time()
    t0 = bfs(time_map, start, end)
    print(f"Part 1: {t0}")  # part 1: 286
    bench_t2 = time.time()
    t1 = bfs(time_map, start, end, t0=t0, forward=False)
    t2 = bfs(time_map, start, end, t0=t1, forward=True)
    print(f"Part 2: {t2}")  # part 2: 820
    bench_t3 = time.time()

    print(f"Runtime -- Parsing {bench_t1-bench_t0:.3} | Part 1 {bench_t2-bench_t1:.3} | Part 2 {bench_t3-bench_t2:.3}")


if __name__ == "__main__":
    main()
