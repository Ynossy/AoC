def find_marker(line, n):
    i = 0
    while len(set(line[i : i + n])) != n:
        i += 1
    return i + n


def main():
    with open("input.txt") as f:
        line = f.readline()
    print(f"Part 1: {find_marker(line, 4)}")  # 1766
    print(f"Part 2: {find_marker(line, 14)}")  # 2383


if __name__ == "__main__":
    main()
