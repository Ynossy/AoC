# %%
with open("input.txt") as f:
    machines = []
    for line in f.read().strip().split("\n"):
        raw = [x[1:-1] for x in line.split(" ")]
        light = sum(2**i for i in range(len(raw[0])) if raw[0][i] == "#")
        joltage = [int(n) for n in raw[-1].split(",")]
        buttons = [sum(2 ** int(n) for n in x.split(",")) for x in raw[1:-1]]
        buttons_p2 = []
        for x in raw[1:-1]:
            b_p2 = [0 for _ in range(len(raw[0]))]
            for n in x.split(","):
                b_p2[int(n)] += 1
            buttons_p2.append(b_p2)
        machines.append([light, buttons, joltage, buttons_p2])
# %%
result = 0
for machine in machines:
    min_buttons = 42069
    for n in range(2 ** len(machine[1])):
        light_state = 0
        buttons = 0
        for bit in range(len(machine[1])):
            if n & 2**bit > 0:
                buttons += 1
                light_state ^= machine[1][bit]
        if light_state == machine[0] and buttons < min_buttons:
            min_buttons = buttons
    result += min_buttons

print(f"Part 1: {result}")  # 459
# %%
from scipy.optimize import milp, LinearConstraint
import numpy as np

buttons_sum = 0
for machine in machines:
    A_eq = np.array(machine[3]).T
    b_eq = np.array(machine[2])
    c = np.ones((len(machine[3]),))
    result_ilp = milp(
        c, integrality=c, constraints=LinearConstraint(lb=b_eq, ub=b_eq, A=A_eq)
    )
    buttons_sum += sum(round(x) for x in result_ilp.x)

print(f"Part 2: {buttons_sum}")  # 18687
# %%
