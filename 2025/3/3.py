# %%
with open("input.txt") as f:
    data = f.read().strip().split("\n")


# %%
def getMaxJoltage(bank, num_batteries):
    result = 0
    max_values = [0] * num_batteries
    for i in range(len(bank)):
        joltage = int(bank[i])
        for j in range(num_batteries):
            if joltage > max_values[j] and i < len(bank) - num_batteries + 1 + j:
                max_values[j] = joltage
                max_values[j + 1 :] = [0] * (num_batteries - 1 - j)
                break
    battery_voltage = 0
    for v in max_values:
        battery_voltage = battery_voltage * 10 + v
    result += battery_voltage
    return result


print(f"Part1: {sum(getMaxJoltage(bank, 2) for bank in data)}")  # 16842
print(f"Part2: {sum(getMaxJoltage(bank, 12) for bank in data)}")  # 167523425665348
# %%
