#%%
import numpy as np


def has_symbol(data, y, start, end):
    start_idx = start if start == 0 else start - 1
    end_idx = end if end == len(data[y]) - 1 else end + 1

    if (
        y != 0
        and data[y - 1][start_idx : end_idx + 1].count(".") != end_idx + 1 - start_idx
    ):
        return True

    if (
        y != len(data) - 1
        and data[y + 1][start_idx : end_idx + 1].count(".") != end_idx + 1 - start_idx
    ):
        return True

    if start != 0 and data[y][start - 1] != ".":
        return True

    if end != len(data[y]) - 1 and data[y][end + 1] != ".":
        return True
    return False


def part1(data: list[str]):
    result = 0
    max_y = len(data)
    max_x = len(data[0])
    for y in range(max_y):
        start_idx = 0
        line = data[y]
        for x in range(max_x):
            if line[x].isnumeric() and (x == 0 or not line[x - 1].isnumeric()):
                start_idx = x
            if line[x].isnumeric() and (x + 1 == max_x or not line[x + 1].isnumeric()):
                if int(line[start_idx : x + 1]) == 968:
                    abc = 0
                if has_symbol(data, y, start_idx, x):
                    result += int(line[start_idx : x + 1])
            #         print(f"\033[31m{line[start_idx : x + 1]}\033[0m", end="")
            #     else:
            #         print(f"\033[32m{line[start_idx : x + 1]}\033[0m", end="")
            # elif(not line[x].isnumeric()):
            #     print(line[x], end="")
        # print("")
    return result


def part2(data: list[str]):
    result = 0
    max_y = len(data)
    max_x = len(data[0])
    numbers = [[] for _ in range(max_y)]  # [value, xstart, xend] idx-inclusive
    stars = []  # [y, x]
    for y in range(max_y):
        start_idx = 0
        line = data[y]
        for x in range(max_x):
            if line[x].isnumeric() and (x == 0 or not line[x - 1].isnumeric()):
                start_idx = x
            if line[x].isnumeric() and (x + 1 == max_x or not line[x + 1].isnumeric()):
                numbers[y].append([int(line[start_idx : x + 1]), start_idx, x])
            if line[x] == "*":
                stars.append([y, x])

    for star in stars:
        y, x = star
        adjacent = []
        for dy in range(y - (y > 0), y + (y < len(data)) + 1):
            for n in numbers[dy]:
                value, xstart, xend = n
                if x - (x > 0) <= xstart <= x + (x < len(data[dy])) or x - (
                    x > 0
                ) <= xend <= x + (x < len(data[dy])):
                    adjacent.append(value)
        if len(adjacent) == 2:
            result += adjacent[0] * adjacent[1]
    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().strip().split("\n")
    print(f"Part1: {part1(data)}")  # 553769 too low, 553825 right
    print(f"Part2: {part2(data)}")  # 93994191

# %%
