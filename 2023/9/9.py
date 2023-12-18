import numpy as np


def differentiate_sequences(numbers: list[list[int]]):
    while any(numbers[-1]):
        numbers.append(
            [numbers[-1][i + 1] - numbers[-1][i] for i in range(len(numbers[-1]) - 1)]
        )
    return numbers


def extrapolate(report, part2=False):
    numbers = differentiate_sequences([[int(i) for i in report.split(" ")]])
    for i in reversed(range(len(numbers) - 1)):
        if part2:
            numbers[i].insert(0, numbers[i][0] - numbers[i + 1][0])
        else:
            numbers[i].append(numbers[i][-1] + numbers[i + 1][-1])
    return numbers[0][0 if part2 else -1]


def part1(data: list[str]):
    return sum(extrapolate(report) for report in data)


def part2(data: list[str]):
    return sum(extrapolate(report, True) for report in data)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().strip().split("\n")
    print(f"Part1: {part1(data)}")  # 1798691765
    print(f"Part2: {part2(data)}")  # 1104
