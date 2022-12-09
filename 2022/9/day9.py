import numpy as np
dirs = {'U':[0,1], 'D':[0,-1], 'R':[1,0], 'L':[-1,0]}

def main():
    with open("input.txt") as f:
        moves = [
            (s.split(" ")[0], int(s.split(" ")[1]))
            for s in f.read().strip().split("\n")
        ]
    position = set((0,0))

    H = np.array([0, 0])
    T = np.array([0, 0])

    for move in moves:
        for _ in range(move[1]):
            H = np.add(H, dirs[move[0]])
            if np.linalg.norm(H-T) < 1.5:
                continue
            if T[0] != H[0]:
                T[0] += 1 if T[0] < H[0] else -1
            if T[1] != H[1]:
                T[1] += 1 if T[1] < H[1] else -1
            position.add((T[0],T[1]))

    print(f"Positons covered: {len(position)}") # 5619



if __name__ == "__main__":
    main()
