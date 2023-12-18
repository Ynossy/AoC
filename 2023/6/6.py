import numpy as np
import math


def get_n_winners(t, d):
    zeros = [
        math.floor((t - np.sqrt(t**2 - 4 * d)) / 2 + 1),
        math.ceil((t + np.sqrt(t**2 - 4 * d)) / 2 - 1),
    ]
    return zeros[1] - zeros[0] + 1


def part1(data: list[str]):
    times = [int(t) for t in " ".join(data[0].split()).split(": ")[1].split(" ")]
    records = [int(d) for d in " ".join(data[1].split()).split(": ")[1].split(" ")]
    return math.prod([get_n_winners(times[i], records[i]) for i in range(len(times))])


def part2(data: list[str]):
    time = int("".join(data[0].split()).split(":")[1])
    record = int("".join(data[1].split()).split(":")[1])
    return get_n_winners(time, record)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().strip().split("\n")

    print(f"Part1: {part1(data)}")  # 1312850
    print(f"Part2: {part2(data)}")  # 36749103
