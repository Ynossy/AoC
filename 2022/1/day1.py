import numpy as np


def main():
    with open("input.txt") as f:
        calories = [[int(n) for n in s.splitlines()] for s in f.read().split("\n\n")]
    summed_cals = [np.sum(l) for l in calories]
    summed_cals.sort()
    print(f"Maximal Calories: {summed_cals[-1]}")  # Part 1: 69177
    print(
        f"Top 3 Calories: {summed_cals[-1]+summed_cals[-2]+summed_cals[-3]}"
    )  # Part 2: 207456


if __name__ == "__main__":
    main()
