import numpy as np
from functools import cmp_to_key

directions = {"U": [-1, 0], "R": [0, 1], "D": [1, 0], "L": [0, -1]}


def part1(data: list[list[str]]):
    return 0


def part2(data: list[str]):
    return 0


if __name__ == "__main__":
    with open("example.txt") as f:
        data = [row.split(" ") for row in f.read().strip().split("\n")]
    print(f"Part1: {part1(data)}")  # 0
    print(f"Part2: {part2(data)}")  # 0
