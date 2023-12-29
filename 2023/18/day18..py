import numpy as np


directions = {"U": [-1, 0], "R": [0, 1], "D": [1, 0], "L": [0, -1]}
offset = {"U": "R", "R": "D", "D": "L", "L": "U"}


def get_area(trench):
    area = 0
    for i in range(len(trench)):
        y1, x1 = trench[i]
        y2, x2 = trench[(i + 1) % len(trench)]
        area += (y2 - y1) * (x1 + x2)
    return int(area / 2)


# assume clockwise loop direction and walk outline of integer area
def get_trench(data):
    trench = []
    y, x = 0, 0
    for i in range(len(data)):
        d, length, _ = data[i]
        length = int(length)
        if offset[d] == data[(i + 1) % len(data)][0]:
            length += 1
        if offset[d] == data[(i - 1) % len(data)][0]:
            length -= 1
        dy, dx = directions[d]
        y += dy * length
        x += dx * length
        trench.append([y, x])
    return trench


def part1(data: list[str]):
    return get_area(get_trench(data))


def part2(data: list[str]):
    return get_area(get_trench(data))


if __name__ == "__main__":
    with open("input.txt") as f:
        data = [row.split(" ") for row in f.read().strip().split("\n")]
    print(f"Part1: {part1(data)}")  # 47045
    data2 = [
        [["R", "D", "L", "U"][int(hex[-2])], int(hex[2:-2], 16), 0]
        for _, _, hex in data
    ]
    print(f"Part2: {part2(data2)}")  # 0
