import re


def part1(board_map, instructions):
    # facing is 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^)
    direction = 0
    pos = [0, 0]  # line and position (without offset) in line
    index_on_line = (
        lambda i: pos[1] + board_map[pos[0]][0] - board_map[(i) % len(board_map)][0]
    )
    for i in instructions:
        if i == "R":
            direction = (direction + 1) % 4
            continue
        elif i == "L":
            direction = (direction - 1) % 4
            continue

        for _ in range(int(i)):
            if (
                direction == 0
                and board_map[pos[0]][1][(pos[1] + 1) % len(board_map[pos[0]][1])]
                != "#"
            ):
                # right
                pos[1] = (pos[1] + 1) % len(board_map[pos[0]][1])
            elif (
                direction == 2
                and board_map[pos[0]][1][(pos[1] - 1) % len(board_map[pos[0]][1])]
                != "#"
            ):
                # left
                pos[1] = (pos[1] - 1) % len(board_map[pos[0]][1])
            elif direction == 1:
                # down
                d_line_idx = (pos[0] + 1) % len(board_map)
                d_idx = pos[1] + board_map[pos[0]][0] - board_map[d_line_idx][0]
                if d_idx < 0 or d_idx >= len(board_map[d_line_idx][1]):
                    i = 1
                    while (index_on_line(d_line_idx - i) >= 0) and (
                        index_on_line(d_line_idx - i)
                        < len(board_map[(d_line_idx - i) % len(board_map)][1])
                    ):
                        i += 1
                    d_line_idx = (d_line_idx - i + 1) % len(board_map)
                    d_idx = pos[1] + board_map[pos[0]][0] - board_map[d_line_idx][0]

                d_line = board_map[d_line_idx][1]
                if d_line[d_idx] != "#":
                    pos[0] = d_line_idx
                    pos[1] = d_idx
                else:
                    break
            elif direction == 3:
                # up
                d_line_idx = (pos[0] - 1) % len(board_map)
                d_idx = pos[1] + board_map[pos[0]][0] - board_map[d_line_idx][0]
                if d_idx < 0 or d_idx >= len(board_map[d_line_idx][1]):
                    i = -1
                    while (index_on_line(d_line_idx - i) >= 0) and (
                        index_on_line(d_line_idx - i)
                        < len(board_map[(d_line_idx - i) % len(board_map)][1])
                    ):
                        i -= 1
                    d_line_idx = (d_line_idx - i - 1) % len(board_map)
                    d_idx = pos[1] + board_map[pos[0]][0] - board_map[d_line_idx][0]

                d_line = board_map[d_line_idx][1]
                if d_line[d_idx] != "#":
                    pos[0] = d_line_idx
                    pos[1] = d_idx
                else:
                    break
    return 1000 * (pos[0] + 1) + 4 * (pos[1] + 1 + board_map[pos[0]][0]) + direction


def part2(raw_board, instructions, width):
    # facing is 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^)
    direction = 0
    pos = [0, 0]  # line and position (without offset) in line

    # build cube rotations and connected faces (i.e. rotation matrix for every side and rotate direction vectors on wrapover)
    cube_side = 50
    grid_x = len(raw_board) // cube_side
    grid_y = width // cube_side
    sides = [[None for i in range(grid_y)] for i in range(grid_x)]

    # separate faces
    for i in range(len(raw_board) // cube_side):
        for j in range(len(raw_board[i * cube_side]) // cube_side):
            sides[i][j] = [
                line[j * cube_side : (j + 1) * cube_side]
                for line in raw_board[i * cube_side : (i + 1) * cube_side]
            ]
            if sides[i][j][0].isspace():
                sides[i][j] = None
    print(sides)

    for i in instructions:
        pass
    return 1000 * (pos[0] + 1) + 4 * (
        pos[1] + 1
    )  # ? + board_map[pos[0]][0]) + direction


def main():
    with open("22/input.txt") as f:
        lines = f.read().split("\n")
    instructions = re.split("(\D)", lines[-2])
    # save map as offset from left and stripped string
    width = max([len(l) for l in lines[:-3]])
    board_map = [
        [len(line) - len(line.lstrip()), list(line.strip())] for line in lines[:-3]
    ]
    # print(f"Result 1: {part1(board_map, instructions)}")
    # 153056 too high, 133044 too high
    # 26356 too low
    # 26556
    # 26558 right
    print(f"Result 2: {part2(lines[:-3], instructions, width)}")


if __name__ == "__main__":
    main()
