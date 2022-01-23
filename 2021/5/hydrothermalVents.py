#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# input = "EXAMPLE"
input = "TASK"

if input == "EXAMPLE":
    df = pd.read_csv("example.txt", names=["x1", "n", "y2"])
else:
    df = pd.read_csv("input.txt", names=["x1", "n", "y2"])
df[["y1", "x2"]] = df["n"].str.replace(" -> ", " ").str.split(" ", expand=True)
df = df.drop("n", axis=1)
df = df.astype(int)

#%% First Task, no beauty
if input == "EXAMPLE":
    sea_map = np.zeros((10, 10))  # example
else:
    sea_map = np.zeros((1000, 1000))  # empirical size of the map


for i, row in df.iterrows():
    if row["x1"] == row["x2"]:
        if row["y1"] < row["y2"]:
            sea_map[row["y1"] : row["y2"] + 1, row["x1"]] += 1
        else:
            sea_map[row["y2"] : row["y1"] + 1, row["x1"]] += 1

    elif row["y1"] == row["y2"]:
        if row["x1"] < row["x2"]:
            sea_map[row["y1"], row["x1"] : row["x2"] + 1] += 1
        else:
            sea_map[row["y1"], row["x2"] : row["x1"] + 1] += 1

print(f"First Exercise: overlapping spots {np.sum(sea_map>1)}")
# plt.matshow(sea_map)
# plt.gcf().set_dpi(150)

# %% Second Task, much beauty
if input == "EXAMPLE":
    sea_map = np.zeros((10, 10))  # example
else:
    sea_map = np.zeros((1000, 1000))  # empirical size of the map

for i, row in df.iterrows():
    i_x = np.linspace(row["x1"], row["x2"], np.abs(row["x1"] - row["x2"]) + 1).astype(
        int
    )
    i_y = np.linspace(row["y1"], row["y2"], np.abs(row["y1"] - row["y2"]) + 1).astype(
        int
    )

    sea_map[i_y, i_x] += 1

print(f"Second Exercise: overlapping spots {np.sum(sea_map>1)}")
plt.matshow(sea_map)
# plt.gcf().set_dpi(300)
plt.show()
# %%
