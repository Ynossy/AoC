import heapq
import time

directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 0:North, 1:East, 2:South, 3:West


def find_path(data, n_fw_min, n_fw_max):
    min_heap = []
    heapq.heappush(min_heap, (0, 0, 0, 2, -1))  # [heatloss, y, x, heading, distance]
    distances = [
        [[float("inf")] * 2 * n_fw_max for _ in range(len(data[0]))]
        for _ in range(len(data))
    ]
    distances[0][0] = [0] * 2 * n_fw_max  # every stepcount v and h
    while (
        min_heap[0][1] != len(data) - 1
        or min_heap[0][2] != len(data[0]) - 1
        or min_heap[0][4] < n_fw_min - 1
    ):
        loss, y, x, heading, d = heapq.heappop(min_heap)
        for ddir in [-1, 0, 1]:
            if ddir == 0 and d >= n_fw_max - 1:
                continue
            elif ddir != 0 and 0 <= d < n_fw_min - 1:
                continue
            new_dir = (heading + ddir) % 4
            new_d = d + 1 if ddir == 0 else 0
            state_idx = (new_dir % 2) * n_fw_max + new_d
            dy, dx = directions[new_dir]
            if (
                0 <= y + dy < len(data)
                and 0 <= x + dx < len(data[0])
                and loss + data[y + dy][x + dx] < distances[y + dy][x + dx][state_idx]
            ):
                distances[y + dy][x + dx][state_idx] = loss + data[y + dy][x + dx]
                heapq.heappush(
                    min_heap,
                    (
                        loss + data[y + dy][x + dx],
                        y + dy,
                        x + dx,
                        new_dir,
                        new_d,
                    ),
                )
    return heapq.heappop(min_heap)[0]


def part1(data: list[list[int]]):
    return find_path(data, 1, 3)


def part2(data: list[list[int]]):
    return find_path(data, 4, 10)


if __name__ == "__main__":
    t = time.time()
    with open("example2.txt") as f:
        data = [[int(c) for c in row] for row in f.read().strip().split("\n")]
    print(f"Part1: {part1(data)}")  # 646 too high, 635 right
    print(f"Part2: {part2(data)}")  # 735 too high, 737 too high, 734 from reddit right?
    print(f"Runtime: {time.time()-t}")
