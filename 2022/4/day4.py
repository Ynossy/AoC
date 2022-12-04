import numpy as np


def part1(data):
    # 55 too high
    # 524 right
    print(
        f"Part1: {sum((i[0] <= i[2] and i[3] <= i[1]) or (i[0] >= i[2] and i[3] >= i[1]) for i in data)}"
    )


def part2(data):
    # 798
    print(
        f"Part2: {sum(i[0]<=i[2]<=i[1] or i[0]<=i[3]<=i[1] or i[2]<=i[0]<=i[3] or i[2]<=i[1]<=i[3] for i in data)}"
    )


def main():
    # with open("example.txt") as f:
    with open("input.txt") as f:
        lines = f.read().splitlines()
    data = [[int(c) for c in x.replace("-", ",").split(",")] for x in lines]
    part1(data)
    part2(data)


if __name__ == "__main__":
    main()
