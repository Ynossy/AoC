def count_line(y, sensors, beacons, min_c, max_c):
    # find segments for all sensors:
    segments = [
        [s[0] - s[2] + abs(y - s[1]), s[0] + s[2] - abs(y - s[1])]
        for s in sensors
        if abs(y - s[1]) <= s[2]
    ]
    segments.sort(key=lambda s: s[0])
    idx = min_c
    x_beacon = 0
    free_spots = 0
    beacons_on_line = sum([b[1] == y for b in beacons])

    for s in segments:
        if s[0] >= idx:
            if s[0] > idx:
                x_beacon = s[0] - 1  # capture empty hole for part 2
            free_spots += 1 + min(s[1], max_c) - s[0]
            idx = s[1] + 1
        elif s[1] >= idx:
            free_spots += min(s[1], max_c) - idx + 1
            idx = s[1] + 1
        if s[1] > max_c:
            return free_spots, x_beacon
    return free_spots - beacons_on_line, -1


def main():
    with open("input.txt") as f:
        coords = [
            [
                int(s.split(" ")[2][2:-1]),
                int(s.split(" ")[3][2:-1]),
                int(s.split(" ")[8][2:-1]),
                int(s.split(" ")[9][2:]),
            ]
            for s in f.read().strip().split("\n")
        ]
    sensors = [
        [c[0], c[1], abs(c[0] - c[2]) + abs(c[1] - c[3])] for c in coords
    ]  # [x, y, d]
    beacons = set((c[2], c[3]) for c in coords)  # [x, y]

    print(
        f"Part1: {count_line(2000000, sensors, beacons, -float('inf'), float('inf'))[0]}"
    )  # 5286569 too high but on line 10, lol; 4951427 right
    # print(count_line(10, sensors, beacons, -float("inf"), float("inf")))

    # for i in range(20):
    #     count_line(i, sensors, beacons, 0, 20)
    print("This takes like 2 minutes, yolo")
    for i in range(4000000):
        print(i, end="\r")
        count, x = count_line(i, sensors, beacons, 0, 4e6)
        if count == 4e6:
            print(f"Part 2: {x*4000000+i}")  # 13029714573243
            break


if __name__ == "__main__":
    main()
