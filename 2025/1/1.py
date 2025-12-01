# %%
with open("input.txt") as f:
    data = [int(x[1:]) if x[0] == "R" else -int(x[1:]) for x in f.readlines()]

dial = 50
password = 0
for r in data:
    dial = (dial + r) % 100
    password += dial == 0

print(f"Part 1 Password: {password}")  # 964

# %%
dial = 50
password = 0
for clicks in data:
    if clicks > 0:
        password += (dial + clicks) // 100
    else:
        password += ((100 - dial) % 100 - clicks) // 100
    dial = (dial + clicks) % 100

print(f"Part 2 Password: {password}")  # 5872

# %%
