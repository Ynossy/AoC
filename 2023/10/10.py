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


def part1(data: list[list[str]], path_map: list[list[str]]):
    pad_map(data)
    pad_map(path_map)
    idx = [[i, line.index("S")] for i, line in enumerate(data) if "S" in line][0]
    direction = [
        x
        for x in dirs.keys()
        if x in pipes[data[idx[0] + dirs[x][0]][idx[1] + dirs[x][1]]].keys()
    ][0]
    starting_dir = direction
    steps = 0
    while True:
        path_map[idx[0]][idx[1]] = data[idx[0]][idx[1]]
        idx[0], idx[1] = idx[0] + dirs[direction][0], idx[1] + dirs[direction][1]
        if data[idx[0]][idx[1]] == "S":
            break
        steps += 1
        direction = pipes[data[idx[0]][idx[1]]][direction]

    # patch start field to pipe for part 2
    starting_dir = {"N": "S", "S": "N", "W": "E", "E": "W"}[starting_dir]
    for pipe in pipes.keys():
        if starting_dir in pipes[pipe] and direction in pipes[pipe]:
            path_map[idx[0]][idx[1]] = pipe
    return int((steps + 1) / 2)


def part2(path_map: list[str]):
    area = 0
    for d in path_map:
        inside = False
        last_cut = None
        for c in d:
            if c in ["|", "L", "F"] or (last_cut == 'L' and c == 'J') or (last_cut == 'F' and c == '7'):
                inside = not inside
                last_cut = c
            if inside and c == ".":
                area += 1
    return area


if __name__ == "__main__":
    with open("input.txt") as f:
        data = [list(s) for s in f.read().strip().split("\n")]
        path_map = [["." for _ in range(len(l))] for l in data]
    print(f"Part1: {part1(data, path_map)}")  # 6649
    print(f"Part2: {part2(path_map)}")  # 601
