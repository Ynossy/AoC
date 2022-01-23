#%%
# Task: target area: x=209..238, y=-86..-59
Ax = [209, 238]
Ay = [-86, -59]

# Example:
# Ax = [20, 30]
# Ay = [-10, -5]

#%% part 1
# The probe passes through (x,0) a second time when throws up
# -> downwards speed = initial speed -1
y_speed_max = (0 - Ay[0]) - 1
max_height = y_speed_max * (y_speed_max + 1) / 2

print(f"Maximal Speed: {y_speed_max} with height {max_height}")
# %% part 2 - brute force
from time import perf_counter

start = perf_counter()

# possible speed ranges:
x_speed_min = 0
x_speed_max = Ax[1]

y_speed_min = Ay[0]
y_speed_max = -Ay[0]

counter = 0

for x in range(x_speed_min, x_speed_max + 1):
    for y in range(y_speed_min, y_speed_max + 1):
        vx = x
        vy = y
        px = 0
        py = 0
        for i in range(200):
            px += vx
            py += vy
            vx = vx - 1 if vx > 0 else vx
            vy -= 1
            if px > Ax[1] or py < Ay[0]:
                break
            elif Ax[0] <= px <= Ax[1] and Ay[0] <= py <= Ay[1]:
                counter += 1
                break

print(f"Runtime: {perf_counter()-start}")
print(f"Number of initial conditions: {counter}")


# %%
