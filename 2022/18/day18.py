def main():
    with open("input.txt") as f:
        cubes = [
            [int(n) for n in s.strip().split(",")] for s in f.read().strip().split("\n")
        ]
    x_min = (
        min([cube[0] for cube in cubes]) - 1
    )  # pad with 1 empty cube for easy indexing
    y_min = min([cube[1] for cube in cubes]) - 1
    z_min = min([cube[2] for cube in cubes]) - 1
    x_dim = max([cube[0] for cube in cubes]) - x_min + 2
    y_dim = max([cube[1] for cube in cubes]) - y_min + 2
    z_dim = max([cube[2] for cube in cubes]) - z_min + 2

    obsidian = [[[0 for z in range(z_dim)] for y in range(y_dim)] for x in range(x_dim)]

    for x, y, z in cubes:
        obsidian[x - x_min][y - y_min][z - z_min] = 1
    free_sides = 0
    d = ([1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1])
    for x, y, z in cubes:
        free_sides += 6 - sum(
            [
                obsidian[x - x_min + dp[0]][y - y_min + dp[1]][z - z_min + dp[2]]
                for dp in d
            ]
        )
    print(f"Part 1: {free_sides}")  # 4320

    stack = [[0, 0, 0]]
    surface = 0
    while stack:
        x, y, z = stack.pop(0)
        obsidian[x][y][z] = -1
        for dx, dy, dz in d:
            if 0 <= x + dx < x_dim and 0 <= y + dy < y_dim and 0 <= z + dz < z_dim:
                if (
                    obsidian[x + dx][y + dy][z + dz] == 0
                    and [x + dx, y + dy, z + dz] not in stack
                ):
                    stack.append([x + dx, y + dy, z + dz])
                elif obsidian[x + dx][y + dy][z + dz] == 1:
                    surface += 1
    print(f"Part 2: {surface}")  # 2456


if __name__ == "__main__":
    main()
