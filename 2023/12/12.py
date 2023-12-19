from tqdm import tqdm

lut = None


def place_springs(m: str, groups: list[int], cache=False):
    global lut
    if cache: # initialize cache
        lut = [[None for _ in range(len(m))] for _ in range(len(groups))]
    if lut and lut[-len(groups)][-len(m)] is not None:
        return lut[-len(groups)][-len(m)]  # infinite speedup
    if not groups:
        return "#" not in m
    if len(m) < sum(groups) + len(groups) - 1:
        return 0  # 50% speedup
    combinations = 0
    g_len = groups[0]
    first_spring = m.find("#")
    qs = [  # all '?' up to (and including) the first '#' are candidates for placement
        i
        for i, c in enumerate(m)
        if c in ["?", "#"] and (first_spring == -1 or i <= first_spring)
    ]
    for q in qs:
        if q + g_len > len(m):
            break
        if m[q : q + g_len].find(".") == -1 and (
            q + g_len == len(m) or m[q + g_len] != "#"
        ):
            combinations += place_springs(m[q + g_len + 1 :], groups[1:])
    if lut:
        lut[-len(groups)][-len(m)] = combinations
    return combinations


def part1(data: list[list[str, list[int]]]):
    return sum(place_springs(m, group) for m, group in data)


def part2(data: list[list[str, list[int]]]):
    return sum(place_springs(m + f"?{m}" * 4, group * 5, True) for m, group in data)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = [
            [l.split(" ")[0], [int(n) for n in l.split(" ")[1].split(",")]]
            for l in f.read().strip().split("\n")
        ]
    print(f"Part1: {part1(data)}")  # 6871
    print(f"Part2: {part2(data)}")  # 2043098029844
