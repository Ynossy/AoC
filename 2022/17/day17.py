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

    tetris = [[1, 1, 1, 1, 1, 1, 1]]
    flow_idx = 0
    rock_idx = 0
    for _ in range(2022):
        rock_center = [0, 2]
        while True:  # falling
            move = 1 if flow[flow_idx] == ">" else -1
            flow_idx = (flow_idx + 1) % len(flow)
            #move l/r
            if 0 <= rock_center[0] + move < 7:
                rock_center[0] += move
            # check downwards
            
        rock_idx = (rock_idx + 1) % 5


if __name__ == "__main__":
    main()
