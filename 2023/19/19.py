import numpy as np


def parse_ratings(line: str):
    line = line.split("{x=")[1]
    x, line = line.split(",m=")
    m, line = line.split(",a=")
    a, line = line.split(",s=")
    s, line = line.split("}")
    return {"x": int(x), "m": int(m), "a": int(a), "s": int(s)}


def parse_workflow(line: str):
    sep = line.find(",")
    if sep == -1:
        return lambda xmas: line
    cond, cond_true = line[:sep].split(":")
    cond_false = line[sep+1:]
    if ">" in cond:
        var, n = cond.split(">")
        return lambda xmas: cond_true if xmas[var]>int(n) else parse_workflow(cond_false)(xmas)
    elif "<" in cond:
        var, n = cond.split("<")
        op = "<"
        return lambda xmas: cond_true if xmas[var]<int(n) else parse_workflow(cond_false)(xmas)
    else:
        print(f"invalid operator: {op}")
        return None


def part1(workflows, ratings):
    accepted = 0
    for rating in ratings:
        result = workflows["in"](rating)
        while result not in ["R", "A"]:
            result = workflows[result](rating)
        if result == "A":
            accepted += sum(rating.values())
    return accepted


def part2(workflows, ratings):
    return 0


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().strip().split("\n\n")
    workflows = {
        x.split("{")[0]: parse_workflow(x.split("{")[1][:-1])
        for x in data[0].split("\n")
    }
    ratings = [parse_ratings(s) for s in data[1].split("\n")]
    print(f"Part1: {part1(workflows, ratings)}")  # 0
    print(f"Part2: {part2(workflows, ratings)}")  # 0
