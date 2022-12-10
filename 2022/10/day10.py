def draw(image):
    for i in range(6):
        print("".join(image[i * 40 : (i + 1) * 40]))


def cycle(x, c, signalsum, image):
    image[c] = "#" if x - 1 <= c % 40 <= x + 1 else "."
    c += 1
    if (c - 20) % 40 == 0:
        signalsum += c * x
    return c, signalsum


def main():
    with open("input.txt") as f:
        instructions = [
            (s.split()[0], int(s.split()[1]) if len(s.split()) > 1 else None)
            for s in f.read().strip().split("\n")
        ]
    x = 1
    c = signalsum = 0
    image = ["." for _ in range(6 * 40)]

    for i in instructions:
        c, signalsum = cycle(x, c, signalsum, image)
        if i[0] == "addx":
            c, signalsum = cycle(x, c, signalsum, image)
            x += i[1]

    print(f"Part 1: {signalsum}")  # 12460
    draw(image)  # EZFPRAKL


if __name__ == "__main__":
    main()
