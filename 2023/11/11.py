import numpy as np
from scipy.spatial.distance import cdist


def expand(data: np.ndarray, n: int):
    stars = np.vstack(np.where(data)).T
    expansion = np.zeros(stars.shape)
    for r in np.argwhere(data.sum(axis=1) == 0).flatten():
        expansion[stars[:, 0] > r, 0] += n
    for c in np.argwhere(data.sum(axis=0) == 0).flatten():
        expansion[stars[:, 1] > c, 1] += n
    stars = stars + expansion
    return int((cdist(stars, stars, metric="cityblock") / 2).sum())


if __name__ == "__main__":
    with open("input.txt") as f:
        data = np.array(
            [[int(c == "#") for c in s] for s in f.read().strip().split("\n")]
        )
    print(f"Part1: {expand(data, 1)}")  # 9418609
    print(f"Part2: {expand(data, 999999)}")  # 593821230983
