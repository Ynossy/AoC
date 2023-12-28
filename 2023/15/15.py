def hash(s: str):
    return sum(ord(c) * 17 ** (len(s) - n) % 256 for n, c in enumerate(s)) % 256


def part1(data: str):
    return sum(hash(instruction) for instruction in data.split(","))


def part2(data: str):
    boxes = {i: [] for i in range(256)}
    for instruction in data.split(","):
        op = "=" if "=" in instruction else "-"
        label, focal = instruction.split(op)
        idx = hash(label)
        if "=" in instruction:
            for e in boxes[idx]:
                if e[0] == label:
                    e[1] = focal
                    break
            else:
                boxes[idx].append([label, focal])
        elif "-" in instruction:
            for e in boxes[idx]:
                if e[0] == label:
                    boxes[idx].remove(e)

        else:
            print("invalid instruction: ", instruction)

    return sum((i+1)*(n+1)*int(b[1]) for i in range(256) for n,b in enumerate(boxes[i]))


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().strip()
    print(f"Part1: {part1(data)}")  # 510273
    print(f"Part2: {part2(data)}")  # 212449
