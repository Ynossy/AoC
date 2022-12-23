def print_cave(cave):
    for s in reversed(cave):
        for c in s:
            if c:
                print("#", end="")
            else:
                print(".", end="")
        print("")


# adjacent = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

nswe = [(-1, -1), (-1, 0), (-1, 1), 
        (1, 1), (1, 0), (1, -1),
        (1, -1), (0, -1), (-1,-1),
        (-1, 1), (0, 1), (1, 1)]


def main():
    with open("input.txt") as f:
        cave = [[1 if c == "#" else 0 for c in s] for s in f.read().strip().split("\n")]
    elves = set(
        [(i, j) for i in range(len(cave)) for j in range(len(cave[0])) if cave[i][j]]
    )
    current_pos = elves.copy()
    for i in range(10):
        # print(current_pos)
        next_pos = {}
        next_pos_set = set()
        duplicates_set = set()
        for elve in current_pos:
            if not any(
                [(elve[0] + dp[0], elve[1] + dp[1]) in current_pos for dp in nswe]
            ):
                next_pos[elve] = elve
                continue
            for j in range(4):
                if not any(
                    [
                        (
                            elve[0] + nswe[((i + j) * 3 + di) % 12][0],
                            elve[1] + nswe[((i + j) * 3 + di) % 12][1],
                        )
                        in current_pos
                        for di in range(3)
                    ]
                ):
                    next_pos[elve] = (
                        elve[0] + nswe[((i + j) * 3 + 1) % 12][0],
                        elve[1] + nswe[((i + j) * 3 + 1) % 12][1],
                    )
                    break
            if next_pos.get(elve) is None:
                next_pos[elve] = elve
            if next_pos[elve] in next_pos_set:
                duplicates_set.add(next_pos[elve])
            else:
                next_pos_set.add(next_pos[elve])
        current_pos = set([next_pos[elve] if next_pos[elve] not in duplicates_set else elve for elve in current_pos])    
        # print(next_pos)
    x_diff = max([p[0] for p in current_pos])- min([p[0] for p in current_pos])+1
    y_diff = max([p[1] for p in current_pos])- min([p[1] for p in current_pos])+1
    print(x_diff,y_diff, x_diff*y_diff-len(current_pos)) # Part 1: 4049



if __name__ == "__main__":
    main()
