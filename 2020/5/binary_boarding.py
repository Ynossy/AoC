#%%
import numpy as np
with open("input.txt") as f:
   data = [s.strip().replace("F","0").replace("B","1").replace("L","0").replace("R","1") for s in f.readlines()]
   row_col = np.array([[int(s[:7],2),int(s[7:],2)] for s in data])

seat_ids = row_col[:,0]*8+row_col[:,1]
print(f"Max seat ID: {np.max(seat_ids)}")

seat_ids.sort()
seat_idx = np.argmax(np.diff(seat_ids))
print(f"Missing Seat ID: {seat_ids[seat_idx]+1}")
# %%