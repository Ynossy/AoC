#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv("input.txt", delimiter=" ", names=["dir", "amount"])

#%% First Part
# forwards
forward = df["amount"].loc[df["dir"] == "forward"]
print(f"Moving forward by {forward.sum()}")

up = df["amount"].loc[df["dir"] == "up"]
print(f"Moving up by {up.sum()}")

down = df["amount"].loc[df["dir"] == "down"]
print(f"Moving down by {down.sum()}")

print(
    f"result = {forward.sum()}*({down.sum()}-{up.sum()})= {forward.sum()*(down.sum()-up.sum())}"
)
# %% Second Part
x = np.zeros((df.value_counts(df["dir"] == "forward")[1] + 1,))
y = np.zeros((df.value_counts(df["dir"] == "forward")[1] + 1,))
idx = 1
aim = 0
for i, row in df.iterrows():
    if row["dir"] == "forward":
        x[idx] = x[idx - 1] + row["amount"]
        y[idx] = y[idx - 1] + aim * row["amount"]
        idx += 1
    elif row["dir"] == "up":
        aim -= row["amount"]
    elif row["dir"] == "down":
        aim += row["amount"]
    else:
        print("what?")

# fig = px.line(x=x,y=y)
# fig.show()
print(f"Final position: X: {x[-1]}, Y: {y[-1]}, Result = {x[-1]*y[-1]}")


# %%
