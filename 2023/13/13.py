import numpy as np


def get_v_mirror(pattern: list[str], errors=0):
    for i in range(len(pattern[0]) - 1):
        if (
            sum(pattern[j][i] != pattern[j][i + 1] for j in range(len(pattern)))
            <= errors
            and v_sym_errors(pattern, i) == errors
        ):
            return i + 1
    return 0


def v_sym_errors(pattern: list[str], idx):
    return sum(
        sum(pattern[j][idx - i] != pattern[j][idx + i + 1] for j in range(len(pattern)))
        for i in range(min(idx + 1, len(pattern[0]) - idx - 1))
    )


def part1(data: list[list[str]]):
    return sum(get_v_mirror(pattern) + 100 * get_v_mirror(list(zip(*pattern))) for pattern in data)


def part2(data: list[list[str]]):
    return sum(
        get_v_mirror(pattern, 1) + 100 * get_v_mirror(list(zip(*pattern)), 1) for pattern in data
    )


if __name__ == "__main__":
    with open("input.txt") as f:
        data = [m.split("\n") for m in f.read().strip().split("\n\n")]
    print(f"Part1: {part1(data)}")  # 30575
    print(f"Part2: {part2(data)}")  # 37478
