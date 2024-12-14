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


def runTask(part2=False):
    buttons = []
    for m in machines:
        matrix = np.array([m[0], m[1]])
        b = 10000000000000 + np.array(m[2]) if part2 else np.array(m[2])
        buttonA, buttonB = b @ np.linalg.inv(matrix)

        if (
            round(buttonA) * m[0][0] + round(buttonB) * m[1][0] == b[0]
            and round(buttonA) * m[0][1] + round(buttonB) * m[1][1] == b[1]
        ):
            buttons.append(3 * round(buttonA) + round(buttonB))
    return sum(buttons)


print(f"Part 1: {runTask()}")
print(f"Part 2: {runTask(True)}")
# %%
