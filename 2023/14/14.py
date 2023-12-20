import copy

dirs = {
    "N": (lambda x: x[0], (-1, 0)),
    "S": (lambda x: -x[0], (1, 0)),
    "W": (lambda x: x[1], (0, -1)),
    "E": (lambda x: -x[1], (0, 1)),
}


def tilt_platform(data, stones: list[list[int]], direction):
    stones.sort(key=dirs[direction][0])
    new_stones = []
    boundary_check = lambda y, x: 0 <= y < len(data) and 0 <= x < len(data[0])
    for y, x in stones:  # stones are ordered from N to S
        dy, dx = dirs[direction][1]
        while boundary_check(y + dy, x + dx) and data[y + dy][x + dx] == ".":
            data[y][x], data[y + dy][x + dx] = ".", "O"
            y += dy
            x += dx
        new_stones.append([y, x])
    return new_stones


def part1(data: list[str], stones):
    stones = tilt_platform(data, stones, "N")
    return sum(len(data) - y for y, _ in stones)


def part2(data: list[str], stones):
    moves = ["N", "W", "S", "E"]
    pattern = []
    search_idx = 0
    search_start = 500
    tries = 1000000000 * 4  # cycles
    for i in range(tries):
        stones = tilt_platform(data, stones, moves[i % len(moves)])
        score = sum(len(data) - y for y, _ in stones)
        if i >= search_start:
            if len(pattern) < 200:
                pattern.append(score)
            search_idx += len(pattern) > 2 and pattern[search_idx] == score
            if search_idx == 100:
                period = i - search_start - 100 + 1
                break
    return pattern[(tries - 1 - search_start) % period]


if __name__ == "__main__":
    with open("input.txt") as f:
        data = [list(s) for s in f.read().strip().split("\n")]
    stones = [
        [i, j]
        for i in range(len(data))
        for j in range(len(data[0]))
        if data[i][j] == "O"
    ]
    print(f"Part1: {part1(copy.deepcopy(data), stones)}")  # 111979
    print(
        f"Part2: {part2(copy.deepcopy(data), stones)}"
    )  # 110859 too high, 103016 too high, 102055 right
