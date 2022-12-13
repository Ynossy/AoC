def compare_int(left, right):
    if left == right:
        return -1
    return left < right


def compare_lists(left, right):
    for i in range(len(left)):
        if i >= len(right):
            return False
        if (x := compare(left[i], right[i])) in [True, False]:
            return x
    if len(left) == len(right):
        return -1
    return True


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return compare_int(left, right)
    if isinstance(left, int):
        left = [left]
    elif isinstance(right, int):
        right = [right]
    return compare_lists(left, right)


def packet_sort(packets):
    # Bubble sort
    ordered = False
    while not ordered:
        ordered = True
        for i in range(len(packets) - 1):
            x = compare(packets[i], packets[i + 1])
            if x == False:
                packets[i], packets[i + 1] = packets[i + 1], packets[i]
                ordered = False


def main():
    with open("input.txt") as f:
        pairs = [
            [eval(p) for p in s.split("\n")] for s in f.read().strip().split("\n\n")
        ]

    indices = [p[0] + 1 for p in enumerate(pairs) if compare(p[1][0], p[1][1])]
    print(f"Part 1: {sum(indices)}")  # 6640 too high; 4505 too low; 6415 right

    packets = [pa for p in pairs for pa in p]
    packets.append([[2]])
    packets.append([[6]])
    packet_sort(packets)
    print(f"Part 2: {(packets.index([[2]])+1)*(packets.index([[6]]) +1)}")


if __name__ == "__main__":
    main()
