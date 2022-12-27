digit = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
inv_digits = {4: "2", 3: "1", 2: "0", 1: "-", 0: "="}


def dec2snafu(n):
    i = 0
    while 5**i < n:
        i += 1
    # add 222222 base 5 and parse it normally as base 5
    n += sum([2 * 5**j for j in range(i)])

    snafu = ""
    for j in reversed(range(i)):
        snafu += inv_digits[n // 5**j]
        n = n % 5**j
    return snafu


def main():
    with open("input.txt") as f:
        numbers = f.read().strip().split("\n")

    decimal_sum = sum(
        [sum([digit[c] * 5**i for i, c in enumerate(reversed(n))]) for n in numbers]
    )

    print(f"Part 1: {dec2snafu(decimal_sum)}")  # Part 1: 122-0==-=211==-2-200


if __name__ == "__main__":
    main()
