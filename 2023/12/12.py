import numpy as np
from tqdm import tqdm


def place_springs(m: str, groups: list[int]):
    global lut
    if lut[-len(groups)][-len(m)] is not None:
        return lut[-len(groups)][-len(m)]
    if not groups:
        return "#" not in m
    if len(m) < sum(groups) + len(groups) - 1:
        return 0
    combinations = 0
    g_len = groups[0]
    first_spring = m.find("#")
    qs = [
        i
        for i, c in enumerate(m)
        if c == "?" and (first_spring == -1 or i < first_spring)
    ]
    if first_spring != -1:
        qs.append(first_spring)
    for q in qs:
        if q + g_len > len(m):
            break
        if m[q : q + g_len].find(".") == -1 and (
            q + g_len == len(m) or m[q + g_len] != "#"
        ):
            combinations += place_springs(m[q + g_len + 1 :], groups[1:])
    lut[-len(groups)][-len(m)] = combinations
    return combinations


def part1(data: list[list[str, list[int]]]):
    return sum(place_springs(m, group) for m, group in data)


def part2(data: list[list[str, list[int]]]):
    global lut
    combinations = 0
    for m, group in tqdm(data):
        m += f"?{m}" * 4
        group *= 5
        lut = [[None for _ in range(len(m))] for _ in range(len(group))]
        combinations += place_springs(m, group)
    return combinations


if __name__ == "__main__":
    with open("input.txt") as f:
        data = [
            [l.split(" ")[0], [int(n) for n in l.split(" ")[1].split(",")]]
            for l in f.read().strip().split("\n")
        ]
    # print(f"Part1: {part1(data)}")  # 6871
    print(f"Part2: {part2(data)}")  # 2043098029844
