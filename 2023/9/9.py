import numpy as np


def part1(data: list[str]):
    result = 0 
    for line in data:
        numbers = [[int(i) for i in line.split(" ")]]
        while any(numbers[-1]):
            numbers.append([numbers[-1][i+1]-numbers[-1][i] for i in range(len(numbers[-1])-1)])
        for i in reversed(range(len(numbers)-1)):
            numbers[i].append(numbers[i][-1]+numbers[i+1][-1])
        result += numbers[0][-1]
    return result


def part2(data: list[str]):
    return 0


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().strip().split("\n")
    print(f"Part1: {part1(data)}")  # 0
    print(f"Part2: {part2(data)}")  # 0
