import numpy as np
from functools import cmp_to_key

values = {"A": 14,"K": 13,"Q": 12,"J": 11,"T": 10,"9": 9,"8": 8,"7": 7,"6": 6,"5": 5,"4": 4,"3": 3,"2": 2}


def get_max_key(d):
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))]


def get_type_value(hand, p2):
    collection = {"A": 0, "K": 0, "Q": 0, "J": 0, "T": 0, "9": 0, "8": 0, "7": 0, "6": 0, "5": 0, "4": 0, "3": 0, "2": 0}
    for i in range(len(hand)):
        collection[hand[i]] += 1
    if p2:
        dJ = collection["J"]
        collection["J"] = 0
        collection[get_max_key(collection)] += dJ
    return sum(x**2 for x in collection.values())


def compare(a, b, p2=False):
    values["J"] = 1 if p2 else 11
    value_a = get_type_value(a, p2)
    value_b = get_type_value(b, p2)
    if value_a > value_b:
        return 1
    elif value_a < value_b:
        return -1
    for i in range(len(a)):
        if values[a[i]] != values[b[i]]:
            return 1 if values[a[i]] > values[b[i]] else -1
    return 0

def compare_p1(a, b):
    return compare(a[0], b[0], p2=False)

def compare_p2(a, b):
    return compare(a[0], b[0], p2=True)


def part1(data: list[str]):
    pairs = [[line.split(" ")[0], int(line.split(" ")[1])] for line in data]
    pairs.sort(key=cmp_to_key(compare_p1))
    return sum((i + 1) * pair[1] for i, pair in enumerate(pairs))


def part2(data: list[str]):
    pairs = [[line.split(" ")[0], int(line.split(" ")[1])] for line in data]
    pairs.sort(key=cmp_to_key(compare_p2))
    return sum((i + 1) * pair[1] for i, pair in enumerate(pairs))


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().strip().split("\n")
    print(f"Part1: {part1(data)}")  # 248396258
    print(f"Part2: {part2(data)}")  # 246436046
