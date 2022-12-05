import copy


def part1(stack, moves):
    # JCMHLVGMG
    stacks = copy.deepcopy(stack)
    for move in moves:
        for _ in range(move[0]):
            stacks[move[2]].append(stacks[move[1]].pop())
    print(f"Result {''.join([s.pop() for s in stacks])}")


def part2(stack, moves):
    # LVMRWSSPZ
    stacks = copy.deepcopy(stack)
    for move in moves:
        temp_stack = [stacks[move[1]].pop() for _ in range(move[0])]
        for _ in range(move[0]):
            stacks[move[2]].append(temp_stack.pop())
    print(f"Result {''.join([s.pop() for s in stacks])}")


def main():
    with open("input.txt") as f:
        lines = f.readlines()

    height = 0
    while len(lines[height]) > 1:
        height += 1

    stacks = []
    for i in range(len(lines[0]) // 4):
        stacks.append(
            [
                c
                for c in [line[1 + 4 * i] for line in reversed(lines[: height - 1])]
                if c != " "
            ]
        )

    moves = []
    for line in lines[height + 1 :]:
        sep = line.split(" ")
        moves.append([int(sep[1]), int(sep[3]) - 1, int(sep[5]) - 1])

    part1(stacks, moves)
    part2(stacks, moves)


if __name__ == "__main__":
    main()
