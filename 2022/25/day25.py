digit = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
inv_digits = {4: "2", 3: "1", 2: "0", 1: "-", 0: "="}


def dec2snafu(n):
    snafu = []
    while n > 0:
        n += 2  # add 2 to get rid of the -2 offset
        snafu.insert(0, inv_digits[n % 5])
        n = n // 5
    return "".join(snafu)


def main():
    with open("input.txt") as f:
        numbers = f.read().strip().split("\n")

    decimal_sum = sum(
        [sum([digit[c] * 5**i for i, c in enumerate(reversed(n))]) for n in numbers]
    )

    print(f"Part 1: {dec2snafu(decimal_sum)}")  # Part 1: 122-0==-=211==-2-200


if __name__ == "__main__":
    main()
