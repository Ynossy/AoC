shapes = {"A": 0, "B": 1, "C": 2, "X": 0, "Y": 1, "Z": 2}


def part1(moves):
    # part 1: 14297
    score = 0
    for move in moves:
        score += 1 + move[1]
        if move[1] == move[0]:
            score += 3
        elif (move[0] + 1) % 3 == move[1]:
            score += 6
    print("Part 1 score: {score}")


def part2(moves):
    # 8573 too low
    # 10498 correct
    score = 0
    for move in moves:
        score += 3 * move[1] + (move[0] + move[1] - 1) % 3 + 1
    print("Part 2 score: {score}")


def main():
    with open("input.txt") as f:
        rounds = [s.strip().split(" ") for s in f.readlines()]
    moves = [[shapes[move] for move in r] for r in rounds]
    # moves = [[0,1],[1,0],[2,2]] # example
    part1(moves)
    part2(moves)


if __name__ == "__main__":
    main()
