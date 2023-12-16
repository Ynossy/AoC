import numpy as np


def intersect_card(card):
    card = card.replace("  ", " ")
    n1, n2 = card.split(": ")[1].split(" | ")
    set_n1 = {int(c) for c in n1.split(" ")}
    set_n2 = {int(c) for c in n2.split(" ")}
    return len(set_n1.intersection(set_n2))


def part1(data: list[str]):
    winners = [intersect_card(card) for card in data]
    return sum(0 if n == 0 else 2 ** (n - 1) for n in winners)


def part2(data: list[str]):
    winners = [intersect_card(card) for card in data]
    card_pile = [1 for _ in range(len(winners))]
    for i in range(len(winners)):
        card_pile[i + 1 : i + 1 + winners[i]] = [
            n + card_pile[i] for n in card_pile[i + 1 : i + 1 + winners[i]]
        ]
    return sum(card_pile)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().strip().split("\n")
    print(f"Part1: {part1(data)}")  # 21558
    print(f"Part2: {part2(data)}")  # 10425665
