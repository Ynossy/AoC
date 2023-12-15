import numpy as np

def part1(data: list[str]):
    bag = {"red": 12, "green":13, "blue":14}
    result = 0
    for id, game in enumerate(data):
        tries = game.split(":")[1].split(";")
        possible = True
        for t in tries:
            cubes = t.strip().split(", ")
            for cube in cubes:
                if int(cube.split(" ")[0]) > bag[cube.split(" ")[1]]:
                    possible = False
        if possible:
            result += id + 1
    return result


def part2(data: list[str]):
    return 0


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().strip().split("\n")
    print(f"Part1: {part1(data)}")  # 0
    print(f"Part2: {part2(data)}")  # 0
