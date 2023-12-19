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
    search_start = 0
    for i in range(6000):
        stones = tilt_platform(data, stones, moves[i%len(moves)])
        score = sum(len(data) - y for y, _ in stones)
        if i== 500:
            pattern = []
            print("Reset: ", i)
        if len(pattern) <100:
            pattern.append(score)
            search_idx = 0
            search_start = i
        else:
            if(search_idx < 100 and pattern[search_idx] == score):
                search_idx += 1
            else:
                search_idx == 0
            if(search_idx == 100):
                # search_idx = 0
                search_idx = 101
                period = i-search_start
                print("Period: ", period)
                # break
    print(pattern[(6000-1-search_start-1-4)%period]) # some offset is happening
    return sum(len(data) - y for y, _ in stones)


if __name__ == "__main__":
    with open("example.txt") as f:
        data = [list(s) for s in f.read().strip().split("\n")]
    stones = [
        [i, j]
        for i in range(len(data))
        for j in range(len(data[0]))
        if data[i][j] == "O"
    ]
    print(f"Part1: {part1(copy.deepcopy(data), stones)}")  # 111979
    print(f"Part2: {part2(copy.deepcopy(data), stones)}")  # 110859 too high
