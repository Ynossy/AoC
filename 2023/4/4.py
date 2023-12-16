import numpy as np

def intersect_card(card):
    card = card.replace("  ", " ")
    n1, n2 = card.split(": ")[1].split(" | ")
    set_n1 = {int(c) for c in n1.split(" ")}
    set_n2 = {int(c) for c in n2.split(" ")}
    winners = len(set_n1.intersection(set_n2))
    return 0 if winners == 0 else 2**(winners-1)

def part1(data: list[str]):
    return sum(intersect_card(card) for card in data)


def part2(data: list[str]):
    return 0


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().strip().split("\n")
    print(f"Part1: {part1(data)}")  # 0
    print(f"Part2: {part2(data)}")  # 0
