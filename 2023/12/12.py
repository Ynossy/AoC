import numpy as np

def place_springs(m: str, groups: list[int]):
    if not groups:
        return "#" not in m
    combinations = 0
    g_len = groups[0]
    first_spring = m.find("#")
    qs = [i for i,c in enumerate(m) if c=='?' and (first_spring == -1 or i < first_spring)]
    if(first_spring != -1): 
        qs.append(first_spring)
    for q in qs:
        if(q+g_len > len(m)):
            break
        if m[q:q+g_len].find(".") == -1 and (q+g_len == len(m) or m[q+g_len]!="#"):
            combinations += place_springs(m[q+g_len+1:], groups[1:])
    return combinations



def part1(data: list[list[str]]):
    return sum(place_springs(m, group) for m, group in data)


def part2(data: list[list[str]]):
    return 0


if __name__ == "__main__":
    with open("input.txt") as f:
        data = [
            [l.split(" ")[0], [int(n) for n in l.split(" ")[1].split(",")]]
            for l in f.read().strip().split("\n")
        ]
    print(f"Part1: {part1(data)}")  # 6871
    print(f"Part2: {part2(data)}")  # 0
