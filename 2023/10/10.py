import numpy as np

pipes = {
    "|": {"N": "N", "S": "S"},
    "-": {"E": "E", "W": "W"},
    "L": {"S": "E", "W": "N"},
    "J": {"S": "W", "E": "N"},
    "7": {"N": "W", "E": "S"},
    "F": {"N": "E", "W": "S"},
    ".": {},
    "S": {},
}

dirs = {"N": [-1, 0], "E": [0, 1], "S": [1, 0], "W": [0, -1]}


def pad_map(data: list[list[str]]):
    for d in data:
        d.insert(0, ".")
        d.append(".")
    data.insert(0, ["." for _ in range(len(data[0]))])
    data.append(["." for _ in range(len(data[0]))])


def part1(data: list[str]):
    pad_map(data)
    idx = [[i, line.index("S")] for i, line in enumerate(data) if "S" in line][0]
    direction = [
        x
        for x in dirs.keys()
        if x in pipes[data[idx[0] + dirs[x][0]][idx[1] + dirs[x][1]]].keys()
    ][0]
    steps = 0
    while True:
        idx[0], idx[1] = idx[0] + dirs[direction][0], idx[1] + dirs[direction][1]
        if data[idx[0]][idx[1]] == "S":
            break
        steps += 1
        direction = pipes[data[idx[0]][idx[1]]][direction]
    return int((steps + 1) / 2)


def part2(data: list[str]):
    return 0


if __name__ == "__main__":
    with open("input.txt") as f:
        data = [list(s) for s in f.read().strip().split("\n")]
    print(f"Part1: {part1(data)}")  # 6649
    print(f"Part2: {part2(data)}")  # 0
