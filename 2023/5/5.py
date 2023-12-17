import numpy as np
from tqdm import tqdm


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


def convert_range(idx_range, mapping):
    mapping.sort(key=lambda x: x[1])
    mapped_ranges = []
    for r_map in mapping:
        if (
            idx_range[0] + idx_range[1] <= r_map[1]
            or r_map[1] + r_map[2] <= idx_range[0]
        ):
            # no overlap
            continue

        if idx_range[0] < r_map[1]:
            # split in 1:1 mapped and rest
            cutoff = r_map[1] - idx_range[0]
            mapped_ranges.append([idx_range[0], cutoff])
            idx_range = [r_map[1], idx_range[1] - cutoff]

        if r_map[1] + r_map[2] < idx_range[0] + idx_range[1]:
            # append mapped first part, continue with remaining
            cutoff = r_map[1] + r_map[2]
            mapped_ranges.append(
                [r_map[0] + idx_range[0] - r_map[1], cutoff - idx_range[0]]
            )
            idx_range = [cutoff, idx_range[0] + idx_range[1] - cutoff]
        else:
            # append all --> done
            mapped_ranges.append([r_map[0] + idx_range[0] - r_map[1], idx_range[1]])
            return mapped_ranges

    mapped_ranges.append(idx_range)
    return mapped_ranges


def get_location_ranges(ranges, maps):
    for mapping in maps:
        mapped_ranges = []
        for r in ranges:
            mapped_ranges += convert_range(r, mapping)
        ranges = mapped_ranges
    return ranges


def part2(seeds, maps):
    ranges = [[seeds[i], seeds[i + 1]] for i in range(0, len(seeds), 2)]

    ranges = get_location_ranges(ranges, maps)
    return min(x[0] for x in ranges)


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
    print(f"Part2: {part2(seeds, maps)}")  # 40484395 too low, reddit correct: 69323688
