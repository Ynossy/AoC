import numpy as np

dirs = {"U": [0, 1], "D": [0, -1], "R": [1, 0], "L": [-1, 0]}


def simulate_rope(moves, n):
    position = set((0, 0))

    rope = [np.array([0, 0]) for i in range(n)]

    for move in moves:
        for _ in range(move[1]):
            rope[0] = np.add(rope[0], dirs[move[0]])
            for i in range(n - 1):
                if np.linalg.norm(rope[i] - rope[i + 1]) < 1.5:
                    continue
                if rope[i + 1][0] != rope[i][0]:
                    rope[i + 1][0] += 1 if rope[i + 1][0] < rope[i][0] else -1
                if rope[i + 1][1] != rope[i][1]:
                    rope[i + 1][1] += 1 if rope[i + 1][1] < rope[i][1] else -1
                if i + 1 == n - 1:
                    position.add((rope[i + 1][0], rope[i + 1][1]))

    print(f"Positons covered: {len(position)}")


def main():
    with open("input.txt") as f:
        moves = [
            (s.split(" ")[0], int(s.split(" ")[1]))
            for s in f.read().strip().split("\n")
        ]

    simulate_rope(moves, 2)  # 5619
    simulate_rope(moves, 10)  # 2376


if __name__ == "__main__":
    main()
