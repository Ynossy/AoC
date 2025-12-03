# %%

with open("input.txt") as f:
    data = f.read().strip().split("\n")
# %%
result = 0
for bank in data:
    max1 = 0
    max2 = 0
    for i in range(len(bank)):
        joltage = int(bank[i])
        if joltage > max1 and i < len(bank) - 1:
            max1 = joltage
            max2 = 0
        elif joltage > max2:
            max2 = joltage
    result += 10 * max1 + max2

print(f"Part1: {result}")  # 16842
# %%

result = 0
for bank in data:
    max_values = [0]*12
    for i in range(len(bank)):
        joltage = int(bank[i])
        for j in range(12):
            if joltage > max_values[j] and i < len(bank) - 12 + 1 + j:
                max_values[j] = joltage
                max_values[j+1:] = [0]*(12-1-j)
                break
        # print(max_values)
    battery_voltage = 0
    for v in max_values:
        battery_voltage = battery_voltage * 10 + v
    result += battery_voltage

print(f"Part1: {result}")  # 167523425665348
# %%
