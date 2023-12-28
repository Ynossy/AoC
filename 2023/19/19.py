import numpy as np


def parse_ratings(line: str):
    line = line.split("{x=")[1]
    x, line = line.split(",m=")
    m, line = line.split(",a=")
    a, line = line.split(",s=")
    s, line = line.split("}")
    return {"x": int(x), "m": int(m), "a": int(a), "s": int(s)}


def parse_workflow(line: str):
    pass


def part1(data: list[str]):
    return 0


def part2(data: list[str]):
    return 0


if __name__ == "__main__":
    with open("example.txt") as f:
        data = f.read().strip().split("\n\n")
    workflows = {
        x.split("{")[0]: parse_workflow(x.split("{")[1][:-1])
        for x in data[0].split("\n")
    }
    print(workflows)
    ratings = [parse_ratings(s) for s in data[1].split("\n")]
    print(ratings)

    print(f"Part1: {part1(data)}")  # 0
    print(f"Part2: {part2(data)}")  # 0
