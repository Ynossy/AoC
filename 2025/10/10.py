# %%
with open("input.txt") as f:
    machines = []
    for line in f.read().strip().split("\n"):
        raw = [x[1:-1] for x in line.split(" ")]
        light = sum(2**i for i in range(len(raw[0])) if raw[0][i] == "#")
        joltage = [int(n) for n in raw[-1].split(",")]
        buttons = [sum(2 ** int(n) for n in x.split(",")) for x in raw[1:-1]]
        machines.append([light, buttons, joltage])
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
