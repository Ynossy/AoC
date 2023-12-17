import numpy as np


def convert(idx, mapping):
    for r in mapping:
        if r[1] <= idx <= r[1] + r[2]:
            return r[0] + idx - r[1]
    return idx


def get_location(seed, maps):
    for mapping in maps:
        seed = convert(seed, mapping)
    return seed


def part1(seeds, maps):
    locations = [get_location(seed, maps) for seed in seeds]
    return min(locations)


def part2(seeds, maps):
    return 0


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().strip().split("\n")

    seeds = [int(i) for i in data[0].split(": ")[1].split(" ")]
    maps = [[] for _ in range(7)]

    map_idx = 0
    data_idx = 3
    while data_idx < len(data):
        if data[data_idx] == "":
            map_idx += 1
            data_idx += 2
            continue
        maps[map_idx].append([int(i) for i in data[data_idx].split(" ")])
        data_idx += 1
    print(f"Part1: {part1(seeds, maps)}")  # 111627841
    print(f"Part2: {part2(seeds, maps)}")  # 0
