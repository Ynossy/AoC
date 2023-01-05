import re


def main():
    with open("input.txt") as f:
        lines = f.read().split("\n")
    instructions = re.split("(\D)", lines[-2])
    # save map as offset from left and stripped string
    board_map = [
        [len(line) - len(line.lstrip()), list(line.strip())] for line in lines[:-3]
    ]

    # facing is 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^)
    direction = 0
    pos = [0, 0]  # line and position (without offset) in line

    for i in instructions:
        if i == "R":
            direction = (direction + 1) % 4
            continue
        elif i == "L":
            direction = (direction - 1) % 4
            continue
        pass
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
                    while (
                        pos[1]
                        + board_map[pos[0]][0]
                        - board_map[(d_line_idx - i) % len(board_map)][0]
                        >= 0
                    ) and (
                        pos[1]
                        + board_map[pos[0]][0]
                        - board_map[(d_line_idx - i) % len(board_map)][0]
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
                    while (
                        pos[1]
                        + board_map[pos[0]][0]
                        - board_map[(d_line_idx - i) % len(board_map)][0]
                        >= 0
                    ) and (
                        pos[1]
                        + board_map[pos[0]][0]
                        - board_map[(d_line_idx - i) % len(board_map)][0]
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

    print(f"Result 1: {1000*(pos[0]+1)+4*(pos[1]+1 + board_map[pos[0]][0])+direction}")
    # 153056 too high, 133044 too high
    # 26356 too low
    # 26556
    # 26558 right


if __name__ == "__main__":
    main()
