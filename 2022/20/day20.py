def swap(numbers, indices, n):
    l = len(numbers)
    idx = indices.index(n)
    shift = numbers[idx] % (l - 1)
    if shift > 0:
        for i in range(idx, idx + shift):
            numbers[i % l], numbers[(i + 1) % l] = numbers[(i + 1) % l], numbers[i % l]
            indices[i % l], indices[(i + 1) % l] = indices[(i + 1) % l], indices[i % l]

    elif shift < 0:
        for i in range(idx, idx + shift, -1):
            numbers[(i - 1) % l], numbers[i % l] = numbers[i % l], numbers[(i - 1) % l]
            indices[(i - 1) % l], indices[i % l] = indices[i % l], indices[(i - 1) % l]


def main():
    with open("input.txt") as f:
        numbers = [int(s.strip()) for s in f.readlines()]
    # print(numbers)
    big_numbers = [811589153 * i for i in numbers]
    indices = [i for i in range(len(numbers))]
    big_indices = indices.copy()
    for i in range(len(numbers)):
        swap(numbers, indices, i)
    idx0 = numbers.index(0)
    print(
        numbers[(idx0 + 1000) % len(numbers)]
        + numbers[(idx0 + 2000) % len(numbers)]
        + numbers[(idx0 + 3000) % len(numbers)]
    )  # Part1: 4578
    for i in range(10):
        print(f"Round: {i}")
        for i in range(len(big_numbers)):
            swap(big_numbers, big_indices, i)
            # print(big_numbers)
    idx0 = big_numbers.index(0)
    print(
        big_numbers[(idx0 + 1000) % len(big_numbers)]
        + big_numbers[(idx0 + 2000) % len(big_numbers)]
        + big_numbers[(idx0 + 3000) % len(big_numbers)]
    )  # Part2: 2159638736133


if __name__ == "__main__":
    main()
