def main():

    with open("input.txt") as f:
        flow = f.readline().strip()
    # define x,y coords of rock blocks: (x_list, y_list, w, h), with center bottom left piece (i.e. x,y >0)
    # x up, y right: X=0 is ground floor
    rocks = []
    #   ####
    rocks.append(([0, 0, 0, 0], [0, 1, 2, 3], 1, 4))
    #   .#.
    #   ###
    #   .#.
    rocks.append(([2, 1, 1, 1, 0], [1, 0, 1, 2, 1], 3, 3))
    #   ..#
    #   ..#
    #   ###
    rocks.append(([2, 1, 0, 0, 0], [2, 2, 2, 1, 0], 3, 3))
    #   #
    #   #
    #   #
    #   #
    rocks.append(([3, 2, 1, 0], [0, 0, 0, 0], 4, 1))
    #   ##
    #   ##
    rocks.append(([1, 1, 0, 0], [0, 1, 0, 1], 2, 2))

    tetris = [
        [1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]
    flow_idx = 0
    rock_idx = 0
    top_idx = 4 # == len(tetris)
    for _ in range(2022):
        rock_center = [top_idx, 2]
        while True:  # falling
            move = 1 if flow[flow_idx] == ">" else -1
            flow_idx = (flow_idx + 1) % len(flow)
            # move l/r
            if 0 <= rock_center[1] + move and rock_center[1] + rocks[rock_idx][3] + move <= 7:
                # print(f"move {'right' if move == 1 else 'left'}")
                free = True
                for dx, dy in zip(rocks[rock_idx][0], rocks[rock_idx][1]):
                    if rock_center[0] + dx >= top_idx:
                        continue
                    x = rock_center[0] + dx
                    y = rock_center[1] + dy + move
                    if tetris[x][y]:
                        free = False
                        break
                if free:
                    rock_center[1] += move
            # check downwards
            free = True
            for dx, dy in zip(rocks[rock_idx][0], rocks[rock_idx][1]):
                if rock_center[0] + dx -1 >= top_idx:
                    continue
                x = rock_center[0] + dx - 1
                y = rock_center[1] + dy
                if tetris[x][y]:
                    free = False
                    break
            if not free:
                for _ in range(4 - top_idx + (rock_center[0] + rocks[rock_idx][2] - 1)):
                    tetris.append([0, 0, 0, 0, 0, 0, 0])
                    top_idx += 1
                for dx, dy in zip(rocks[rock_idx][0], rocks[rock_idx][1]):
                    tetris[rock_center[0]+dx][rock_center[1]+dy] = 1
                break
            rock_center[0] -= 1
        # print_map(tetris)
        rock_idx = (rock_idx + 1) % 5
    print(top_idx-4) # part1: 3100


def print_map(tetris):
    for r in reversed(tetris):
        [print("#" if px else " ", end='') for px in r]
        print("")


if __name__ == "__main__":
    main()
