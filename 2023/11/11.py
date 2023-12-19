import numpy as np
from scipy.spatial.distance import cdist


def part1(data: np.ndarray):
    data = np.insert(
        data,
        np.argwhere(data.sum(axis=1) == 0).flatten(),
        np.zeros((data.shape[1],)),
        axis=0,
    )
    data = np.insert(
        data,
        np.argwhere(data.sum(axis=0) == 0).flatten(),
        np.zeros((data.shape[0], 1)),
        axis=1,
    )
    stars = np.vstack(np.where(data)).T
    return int(cdist(stars, stars, metric="cityblock").sum()/2)


def part2(data: np.ndarray):
    return 0


if __name__ == "__main__":
    with open("input.txt") as f:
        data = np.array(
            [[int(c == "#") for c in s] for s in f.read().strip().split("\n")]
        )
    print(f"Part1: {part1(data)}")  # 9418609
    print(f"Part2: {part2(data)}")  # 0
