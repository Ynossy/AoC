import numpy as np


def part1(data: list[str]):
    stones = [
        [i, j]
        for i in range(len(data))
        for j in range(len(data[0]))
        if data[i][j] == "O"
    ]
    result = 0
    for y, x in stones:  # stones are ordered from N to S
        while y > 0 and data[y - 1][x] == ".":
            data[y][x], data[y - 1][x] = ".", "O"
            y -= 1
        result += len(data) - y
    return result


def part2(data: list[str]):
    return 0


if __name__ == "__main__":
    with open("input.txt") as f:
        data = [list(s) for s in f.read().strip().split("\n")]
    print(f"Part1: {part1(data)}")  # 111979
    print(f"Part2: {part2(data)}")  # 0
