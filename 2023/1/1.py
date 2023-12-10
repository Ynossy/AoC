numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def part1(data):
    digits = [[c for c in b if c.isnumeric()] for b in data]
    return sum(int("".join([i[0], i[-1]])) for i in digits)


def part2(data):
    digits_num = [[[i, int(c)] for i, c in enumerate(b) if c.isnumeric()] for b in data]
    for digits, datapoint in zip(digits_num, data):
        for digit in numbers.keys():
            start = 0
            while (idx := datapoint.find(digit, start)) != -1:
                digits.append([idx, numbers[digit]])
                start = idx + 1
        digits.sort(key=lambda x: x[0])
    return sum(10 * d[0][1] + d[-1][1] for d in digits_num)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().strip().split("\n")
    print(f"Part1: {part1(data)}")  # 54450
    print(f"Part2: {part2(data)}")  # 54265
