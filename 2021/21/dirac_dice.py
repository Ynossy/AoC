#%%
import numpy as np

start = np.array([1, 6])
# start = np.array([4, 8])

# %% part 1
pos = start - 1
score = np.zeros((2,))
dice = np.array([0, 1, 2])
i = 0
while 1:
    pos[i] = (pos[i] + sum(dice % 10 + 1)) % 10
    score[i] += pos[i] + 1
    dice += 3
    if score[i] >= 1000:
        break
    i ^= 1

print(f"Scores: {score}, dice rolles: {dice[0]} times")
print(f"Final score: {min(score)*dice[0]}")

# %% part 2
