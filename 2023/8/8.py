import numpy as np

directions = {"L": 0, "R": 1}


# https://www.scaler.com/topics/lcm-of-two-numbers-in-python/
def gcd(a, b):
    return a if (b == 0) else gcd(b, a % b)


def lcm(a, b):
    return (a / gcd(a, b)) * b


def part1(instructions, maps):
    location = "AAA"
    steps = 0
    while location != "ZZZ":
        location = maps[location][directions[instructions[steps % len(instructions)]]]
        steps += 1
    return steps


def part2(instructions, maps):
    locations = [x for x in maps.keys() if x[2] == "A"]
    periodicy = [0 for _ in locations]
    steps = 0
    while 0 in periodicy:
        locations = [
            maps[location][directions[instructions[steps % len(instructions)]]]
            for location in locations
        ]
        steps += 1
        for i in range(len(locations)):
            if locations[i][2] == "Z" and periodicy[i] == 0:
                periodicy[i] = steps
    result = 1
    for period in periodicy:
        result = lcm(result, period)
    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().strip().split("\n")
    instructions = data[0]
    maps = {}
    for line in data[2:]:
        label, paths = line.split(" = (")
        path_a, path_b = paths[:-1].split(", ")
        maps[label] = (path_a, path_b)
    print(f"Part1: {part1(instructions, maps)}")  # 17287
    print(f"Part2: {part2(instructions, maps)}")  # 18625484023687
