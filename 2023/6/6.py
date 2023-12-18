import numpy as np
import math


def part1(times, records):
    zeros = lambda t,d: [math.floor((t-np.sqrt(t**2-4*d))/2+1), math.ceil((t+np.sqrt(t**2-4*d))/2-1)]
    result = 1
    for i in range(len(times)):
        limits = zeros(times[i], records[i])
        result *= limits[1]-limits[0]+1
    return result


def part2(times, records):
    return 0


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().strip().split("\n")
    times = [int(t) for t in " ".join(data[0].split()).split(": ")[1].split(" ")]
    records = [int(d) for d in " ".join(data[1].split()).split(": ")[1].split(" ")]

    print(f"Part1: {part1(times, records)}")  # 1312850
    print(f"Part2: {part2(times, records)}")  # 0
