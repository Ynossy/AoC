import numpy as np

# order [red green blue]
def parse_max_cubes(game: str) -> dict:
    max_cubes = {"red": 0, "green": 0, "blue": 0}
    for _try in game.split(": ")[1].split("; "):
        for cube in _try.split(", "):
            n, color = cube.split(" ")
            max_cubes[color] = max(max_cubes[color], int(n))
    return max_cubes


def part1(data: list[str]):
    bag = {"red": 12, "green": 13, "blue": 14}
    result = 0
    for id, game in enumerate(data):
        max_cubes = parse_max_cubes(game)
        if all(i <= j for i, j in zip(max_cubes.items(), bag.items())):
            result += id + 1
    return result


def part2(data: list[str]):
    result = 0
    for game in data:
        max_cubes = parse_max_cubes(game)
        result += max_cubes["red"] * max_cubes["blue"] * max_cubes["green"]
    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().strip().split("\n")
    print(f"Part1: {part1(data)}")  # 2278
    print(f"Part2: {part2(data)}")  # 67953
