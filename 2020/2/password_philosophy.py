#%%
with open("input.txt") as f:
    pws = [s.strip().split(": ") for s in f.readlines()]


p1 = p2 = 0
for pw in pws:
    margins, c = pw[0].split(" ")
    low, high = margins.split("-")

    if int(low) <= pw[1].count(c) <= int(high):
        p1 += 1

    if (pw[1][int(low) - 1] == c) ^ (pw[1][int(high) - 1] == c):
        p2 += 1

print(f"Part1 Valid: {p1}, Part2 Valid: {p2}")

# %%
