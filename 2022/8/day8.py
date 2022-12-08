import numpy as np


def is_visible(trees, x, y):
    h = trees[x][y]
    return (
        h > max(trees[x, y + 1 :])
        or h > max(trees[x, :y])
        or h > max(trees[x + 1 :, y])
        or h > max(trees[:x, y])
    )


def score(trees, x, y): # ugly but ok
    score = 1
    t = 1
    for i in range(x+1,len(trees)-1):
        if trees[i,y] < trees[x,y]:
            t += 1
        else:
            break
    score *= t
    t = 1
    for i in reversed(range(1,x)):
        if trees[i,y] < trees[x,y]:
            t += 1
        else:
            break
    score *= t
    t = 1
    for i in range(y+1,len(trees[0])-1):
        if trees[x,i] < trees[x,y]:
            t += 1
        else:
            break
    score *= t
    t = 1
    for i in reversed(range(1,y)):
        if trees[x,i] < trees[x,y]:
            t += 1
        else:
            break
    score *= t
    return score


def main():
    with open("input.txt") as f:
        trees = np.array([[int(i) for i in list(s.strip())] for s in f.readlines()])
    visible = len(trees) * 2 + len(trees[0]) * 2 - 4
    s_max = 0
    for x in range(1, len(trees) - 1):
        for y in range(1, len(trees[0]) - 1):
            visible += is_visible(trees, x, y)
            s = score(trees, x,y)
            if s>s_max:
                s_max = s
    print(f"Part 1: {visible}")  # 1825
    print(f"Part 2: {s_max}") # 235200 


if __name__ == "__main__":
    main()
