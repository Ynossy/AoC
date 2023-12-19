import numpy as np


def get_v_mirror(pattern: list[str]):
    for i in range(len(pattern[0]) - 1):
        if all(
            pattern[j][i] == pattern[j][i + 1] for j in range(len(pattern))
        ) and is_v_symmetric(pattern, i):
            return i + 1
    return 0


def is_v_symmetric(pattern: list[str], idx):
    return all(
        all(pattern[j][idx - i] == pattern[j][idx + i + 1] for j in range(len(pattern)))
        for i in range(min(idx + 1, len(pattern[0]) - idx - 1))
    )


def get_h_mirror(pattern: list[str]):
    for i in range(len(pattern) - 1):
        if pattern[i] == pattern[i + 1] and is_h_symmetric(pattern, i):
            return i + 1
    return 0


def is_h_symmetric(pattern: list[str], idx):
    return all(
        pattern[idx - i] == pattern[idx + 1 + i]
        for i in range(min(idx + 1, len(pattern) - idx - 1))
    )


def part1(data: list[list[str]]):
    return sum(get_v_mirror(pattern) + 100 * get_h_mirror(pattern) for pattern in data)


def part2(data: list[list[str]]):
    return 0


if __name__ == "__main__":
    with open("input.txt") as f:
        data = [m.split("\n") for m in f.read().strip().split("\n\n")]
    print(f"Part1: {part1(data)}")  # 30575
    print(f"Part2: {part2(data)}")  # 0
