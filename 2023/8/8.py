import numpy as np

directions = {"L":0, "R":1}

def part1(data: list[str]):
    instructions = data[0]
    maps = {}
    for line in data[2:]:
        label, paths = line.split(" = (")
        path_a, path_b = paths[:-1].split(", ")
        maps[label] = (path_a, path_b)
    location = "AAA"
    steps = 0
    while location != "ZZZ":
        location = maps[location][directions[instructions[steps%len(instructions)]]]
        steps += 1
    return steps


def part2(data: list[str]):
    return 0


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().strip().split("\n")
    print(f"Part1: {part1(data)}")  # 17287
    print(f"Part2: {part2(data)}")  # 0
