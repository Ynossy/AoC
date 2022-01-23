#%%
# bingo input, find first board to win and get its score

with open("input.txt") as f:
    lines = f.readlines()

import numpy as np

bingos = np.zeros([len(lines) // 6, 5, 5])

# bingo numbers
draws = np.fromstring(lines[0], dtype=int, sep=",")
lines.pop(0)

for i, line in enumerate(lines):
    if i % 6 == 0:  # skip every 6th/empty line
        continue
    bingos[i // 6, i % 6 - 1, :] = np.fromstring(line, dtype=int, sep=" ")
# %% best board
hits = np.zeros([len(lines) // 6, 2, 5])
mask = np.ones(bingos.shape)
for num in draws:
    u, v, w = np.where(bingos == num)
    # mark checked number
    mask[u, v, w] = 0

    # increase row and col counter for drawn number
    hits[u, 0, v] += 1
    hits[u, 1, w] += 1

    if np.sum(hits == 5):
        # evaluate winner score and exit
        board = np.where(hits == 5)
        print(f"Bingo in Board {board[0]}")
        if board[1]:
            # column won
            print(f"Numbers: {bingos[board[0],:,board[2]]}")
        else:
            # row won
            print(f"Numbers: {bingos[board[0],board[2],:]}")
        # sum unmarked numbers and multiply last drawn one
        score = np.sum(bingos[board[0]] * mask[board[0]]) * num
        print(f"Score = {score}")
        break

# %% worst board
hits = np.zeros([len(lines) // 6, 2, 5])
mask = np.ones(bingos.shape)
loser_board = None
for num in draws:
    u, v, w = np.where(bingos == num)
    mask[u, v, w] = 0

    hits[u, 0, v] += 1
    hits[u, 1, w] += 1

    bingoless = np.sum(hits == 5, axis=(1, 2)) == 0
    if np.sum(bingoless) == 1:
        loser_board = np.where(bingoless)

    if loser_board and np.sum(hits[loser_board] == 5):
        pos = np.where(hits[loser_board] == 5)
        print(f"Loser Board {loser_board[0]}")
        if pos[0]:
            print(f"Numbers: {bingos[loser_board,:,pos[1]]}")
        else:
            print(f"Numbers: {bingos[loser_board,pos[1],:]}")
        score = np.sum(bingos[loser_board] * mask[loser_board]) * num
        print(f"Score = {score}")
        break
