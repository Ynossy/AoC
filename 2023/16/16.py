import numpy as np

reflections = {
    "/": {"N": ["E"], "E": ["N"], "S": ["W"], "W": ["S"]},
    "\\": {"N": ["W"], "E": ["S"], "S": ["E"], "W": ["N"]},
    "|": {"N": ["N"], "E": ["N", "S"], "S": ["S"], "W": ["N", "S"]},
    "-": {"N": ["E", "W"], "E": ["E"], "S": ["E", "W"], "W": ["W"]},
    ".": {"N": ["N"], "E": ["E"], "S": ["S"], "W": ["W"]}
}

directions = {"N": [-1, 0], "E": [0, 1], "S": [1, 0], "W": [0, -1]}
max_laser_distance = 800 # increase until  result stays constant

def part1(map: list[str]):
    energized = [[0 for i in range(len(map[0]))] for j in range(len(map))]
    lasers = [(0, -1, "E", 0)]
    while lasers:
        y, x, d, l = lasers.pop()
        dy, dx = directions[d]
        if 0 <= y + dy < len(map) and 0 <= x + dx < len(map[0]) and l<max_laser_distance:
            y += dy
            x += dx
            energized[y][x] += 1
            refracted = reflections[map[y][x]][d]
            for new_d in refracted:
                lasers.append((y, x, new_d, l+1))
    return sum(n>0 for r in energized for n in r)


def part2(data: list[str]):
    return 0


if __name__ == "__main__":
    with open("input.txt") as f:
        data = [list(s) for s in f.read().strip().split("\n")]
    print(f"Part1: {part1(data)}")  # 6883
    print(f"Part2: {part2(data)}")  # 0
