#%%
import re

with open("input.txt") as f:
    passports = [
        {s.split(":")[0]: s.split(":")[1] for s in re.split("\n| ", p)}
        for p in f.read().strip().split("\n\n")
    ]

# %% part 1
entries = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]  # drop cid

valid = 0
for p in passports:
    if all([i in p for i in entries]):
        valid += 1

print(f"Part 1 - Valid are: {valid} passports!")
# %% part 2
from time import perf_counter

start = perf_counter()

entries = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]  # drop cid

valid = 0
for p in passports:
    check = True
    if not all([i in p for i in entries]):
        continue

    if not (
        1920 <= int(p["byr"]) <= 2002
        and 2010 <= int(p["iyr"]) <= 2020
        and 2020 <= int(p["eyr"]) <= 2030
    ):
        check = False
    h = p["hgt"]
    if not (len(h) == 5 and h[-2:] == "cm" and 150 <= int(h[:3]) <= 193) and not (
        len(h) == 4 and h[-2:] == "in" and 59 <= int(h[:2]) <= 76
    ):
        check = False
    if not (p["hcl"][0] == "#" and int(p["hcl"][1:], 16)):
        check = False
    colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if not p["ecl"] in colors:
        check = False
    if not (len(p["pid"]) == 9 and int(p["pid"])):
        check = False

    if check:
        valid += 1

print(f"Part 2 - Valid are: {valid} passports!")
print(f"Runtime: {perf_counter()-start}")

# %%

# %%
