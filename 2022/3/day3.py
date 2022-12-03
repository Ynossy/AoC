import numpy as np


def sum_values(items):
    values = [ord(i) - 96 if ord(i) > 96 else ord(i) - 64 + 26 for i in items]
    return np.sum(values)


def part1(lines):
    items = [
        set(x[: len(x) // 2]).intersection(set(x[len(x) // 2 :])).pop() for x in lines
    ]
    print(sum_values(items))  # 8072


def part2(lines):
    items = [
        set(lines[i]).intersection(lines[i + 1]).intersection(lines[i + 2]).pop()
        for i in range(0, len(lines), 3)
    ]
    print(sum_values(items))  # 2567


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    part1(lines)
    part2(lines)


if __name__ == "__main__":
    main()
