import numpy as np

reflections = {
    "/": {"N": ["E"], "E": ["N"], "S": ["W"], "W": ["S"]},
    "\\": {"N": ["W"], "E": ["S"], "S": ["E"], "W": ["N"]},
    "|": {"N": ["N"], "E": ["N", "S"], "S": ["S"], "W": ["N", "S"]},
    "-": {"N": ["E", "W"], "E": ["E"], "S": ["E", "W"], "W": ["W"]},
    ".": {"N": ["N"], "E": ["E"], "S": ["S"], "W": ["W"]},
}

directions = {"N": [-1, 0], "E": [0, 1], "S": [1, 0], "W": [0, -1]}
max_laser_distance = 100000  # increase until  result stays constant


def get_energized(map, start):
    energized = [[[] for i in range(len(map[0]))] for j in range(len(map))]
    lasers = [start]
    while lasers:
        y, x, d = lasers.pop()
        dy, dx = directions[d]
        if 0 <= y + dy < len(map) and 0 <= x + dx < len(map[0]):
            y += dy
            x += dx
            refracted = reflections[map[y][x]][d]
            for new_d in refracted:
                if new_d not in energized[y][x]:
                    energized[y][x].append(new_d)
                    lasers.append((y, x, new_d))
    return sum(len(n) > 0 for r in energized for n in r)


def part1(map: list[list[str]]):
    return get_energized(map, (0, -1, "E"))


def part2(map: list[list[str]]):
    left = max(get_energized(map, (i, -1, "E")) for i in range(len(map[0])))
    right = max(get_energized(map, (i, len(map[0]), "W")) for i in range(len(map[0])))
    top = max(get_energized(map, (-1, i, "S")) for i in range(len(map)))
    bottom = max(get_energized(map, (len(map), i, "N")) for i in range(len(map)))
    return max(left, right, top, bottom)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = [list(s) for s in f.read().strip().split("\n")]
    import time

    t = time.time()
    print(f"Part1: {part1(data)}")  # 6883
    print(f"Part2: {part2(data)}")  # 7228
    print(f"Runtime: {time.time()-t}s")
