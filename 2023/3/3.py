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
            if line[x].isnumeric() and (
                x + 1 == max_x or not line[x + 1].isnumeric()
            ):
                if(int(line[start_idx : x + 1])==968):
                    abc=0
                if has_symbol(data, y, start_idx, x):
                    result += int(line[start_idx : x + 1])
            #         print(f"\033[31m{line[start_idx : x + 1]}\033[0m", end="")
            #     else:
            #         print(f"\033[32m{line[start_idx : x + 1]}\033[0m", end="")
            # elif(not line[x].isnumeric()):
            #     print(line[x], end="")
        # print("")
    return result

def get_gear_ratio(data, y, x):
    numbers = []
    # left 
    if(x!= 0 and data[y][x-1].isnumeric()):
        start_idx = x-1
        while start_idx>=0 and data[y][start_idx].isnumeric(): start_idx-=1
        numbers.append(int(data[y][start_idx+1:x]))
    
    # right
    if(x!= len(data[y])-1 and data[y][x+1].isnumeric()):
        end_idx = x+1
        while end_idx < len(data[y])-1 and data[y][end_idx].isnumeric(): end_idx+=1
        numbers.append(int(data[y][x+1:end_idx]))

    # top
    # if(y!=0 and )
    # WIP



def part2(data: list[str]):
    result = 0
    max_y = len(data)
    max_x = len(data[0])
    for y in range(max_y):
        for x in range(max_x):
            if(data[y][x]=='*'):
                result += get_gear_ratio(data, y, x)
    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().strip().split("\n")
    print(f"Part1: {part1(data)}")  # 553769 too low, 553825 right
    print(f"Part2: {part2(data)}")  # 0

# %%
