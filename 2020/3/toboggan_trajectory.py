#%%
import numpy as np

with open("input.txt") as f:
    m = np.array(
        [[1 if s == "#" else 0 for s in line.strip()] for line in f.readlines()]
    )

#%% part 1 and 2
slopes = np.array([[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]])

m_rep = np.tile(m, (1, m.shape[0] * (np.max(slopes)+1) // m.shape[1]))

trees = np.zeros((len(slopes),))
for i, slope in enumerate(slopes):
    idx = np.array([0,0])
    while idx[0] < m_rep.shape[0] and idx[1] < m_rep.shape[1]:
        if m_rep[idx[0], idx[1]]:
            trees[i] += 1
        idx += slope

print(f"Part 1 - Num Trees: {trees[1]}")
print(f"Part 2 - {trees} Tree Product: {np.prod(trees)}")

# %%
