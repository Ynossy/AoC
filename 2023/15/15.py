def hash(s: str):
    return sum(ord(c) * 17 ** (len(s) - n) % 256 for n, c in enumerate(s)) % 256


def part1(data: str):
    return sum(hash(instruction) for instruction in data.split(","))


def part2(data: str):
    boxes = {i: {} for i in range(256)}  # dicts keep order
    for instruction in data.split(","):
        op = "=" if "=" in instruction else "-"
        label, focal = instruction.split(op)
        idx = hash(label)
        if op == "=":
            boxes[idx][label] = focal
        else:
            if label in boxes[idx]:
                del boxes[idx][label]
    return sum(
        (i + 1) * (n + 1) * int(b)
        for i in range(256)
        for n, b in enumerate(boxes[i].values())
    )


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().strip()
    print(f"Part1: {part1(data)}")  # 510273
    print(f"Part2: {part2(data)}")  # 212449
