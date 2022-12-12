def find_shortest():
    pass

def main():
    with open("input.txt") as f:
        heightmap = [[ord(i) - ord("a") for i in line] for line in f.read().strip().split("\n")]
    size_x = len(heightmap)
    size_y = len(heightmap[0])
    start = [
        (i, j) for i in range(size_x) for j in range(size_y) if heightmap[i][j] == -14
    ][0]
    start_a = [
        (i, j) for i in range(size_x) for j in range(size_y) if heightmap[i][j] == 0
    ]
    end = [
        (i, j) for i in range(size_x) for j in range(size_y) if heightmap[i][j] == -28
    ][0]
    heightmap[start[0]][start[1]] = 0
    heightmap[end[0]][end[1]] = 25
    path_len = [[1e6 for i in range(size_y)] for j in range(size_x)]
    path_len[start[0]][start[1]] = 0

    stack = [start]
    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    while True:
        pos = stack.pop(0)
        if pos[0] == end[0] and pos[1] == end[1]:
            break
        value = path_len[pos[0]][pos[1]]
        height = heightmap[pos[0]][pos[1]]
        for d in dirs:
            if 0 <= pos[0] + d[0] < size_x and 0 <= pos[1] + d[1] < size_y:
                if (
                    heightmap[pos[0] + d[0]][pos[1] + d[1]] <= height + 1
                    and value + 1 < path_len[pos[0] + d[0]][pos[1] + d[1]]
                ):
                    path_len[pos[0] + d[0]][pos[1] + d[1]] = value + 1
                    stack.append((pos[0] + d[0], pos[1] + d[1]))

    print(path_len[end[0]][end[1]]) # 517


if __name__ == "__main__":
    main()
