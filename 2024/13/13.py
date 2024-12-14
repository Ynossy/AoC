# %%
with open("input.txt") as f:
    data = f.read().strip().split("\n\n")
    machines = []
    for line in data:
        parsing = line.split("\n")
        a = parsing[0][parsing[0].find("X+") + 2 :].split(", Y+")
        b = parsing[1][parsing[1].find("X+") + 2 :].split(", Y+")
        r = parsing[2][parsing[2].find("X=") + 2 :].split(", Y=")
        machines.append(
            [[int(a[0]), int(a[1])], [int(b[0]), int(b[1])], [int(r[0]), int(r[1])]]
        )
# %%
import numpy as np

buttons = []
for m in machines:
    matrix = np.array([m[0], m[1]])
    buttonA, buttonB = m[2] @ np.linalg.inv(matrix)
    if (0.0001 > buttonA % 1 or 0.9999 < buttonA % 1) and (
        0.0001 > buttonB % 1 or 0.9999 < buttonB % 1
    ):
        buttons.append(3 * round(buttonA) + round(buttonB))
    print(buttonA, buttonB)
print(f"Part 1: {sum(buttons)}")

# %%
