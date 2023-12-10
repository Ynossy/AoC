def print_cave(cave):
    for l in cave:
        print("".join(l))


def insert_paths(paths, cave, min_x):
    for p in paths:
        for i in range(len(p) - 1):
            draw_path(cave, p[i], p[i + 1], min_x)


def draw_path(cave, p1, p2, offset_x):
    for x in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
        for y in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
            cave[y][x - offset_x] = "#"


def drop_sand(cave, x, y):
    while True:
        if y + 1 == len(cave):
            return False
        elif cave[y + 1][x] == ".":
            y += 1
        elif x == 0:
            return False
        elif cave[y + 1][x - 1] == ".":
            y += 1
            x -= 1
        elif x == len(cave[0]):
            return False
        elif cave[y + 1][x + 1] == ".":
            y += 1
            x += 1
        else:
            if y == 0:
                print("Source Reached")
                return False
            cave[y][x] = "O"
            return True


def main():
    with open("input.txt") as f:
        paths = [
            [
                (int(xy.split(",")[0]), int(xy.split(",")[1]))
                for xy in s.strip().split(" -> ")
            ]
            for s in f.read().strip().split("\n")
        ]
    # print(paths)
    min_x = min([xy[0] for p in paths for xy in p])
    max_x = max([xy[0] for p in paths for xy in p])  # sand at x = 500
    min_y = 0  # cave starts at y = 0
    max_y = max([xy[1] for p in paths for xy in p])

    len_x = max_x - min_x + 1
    len_y = max_y - min_y + 1
    square_margin = max(0, len_y * 3 - len_x)

    offset_x = min_x - square_margin // 2

    cave = [["." for _ in range(len_x + square_margin)] for _ in range(len_y)]
    insert_paths(paths, cave, offset_x)

    sand_count = 0
    while drop_sand(cave, 500 - offset_x, 0):
        sand_count += 1
    # print_cave(cave)
    print(sand_count)  # 961

    cave.append(["." for _ in range(len_x + square_margin)])
    cave.append(["#" for _ in range(len_x + square_margin)])
    while drop_sand(cave, 500 - offset_x, 0):
        sand_count += 1
    # print_cave(cave)
    print(sand_count + 1)  # 26375


if __name__ == "__main__":
    main()
