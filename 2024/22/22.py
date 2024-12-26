# %%
with open("input.txt") as f:
    buyers = [int(x) for x in f.readlines()]


def nextRng(num):
    num = ((num * 64) ^ num) % 16777216
    num = ((num // 32) ^ num) % 16777216
    num = ((num * 2048) ^ num) % 16777216
    return num


res = 0
diffs = []
prices = []

for i in range(len(buyers)):
    n = buyers[i]
    diff = []
    price = []
    for i in range(2000):
        n2 = nextRng(n)
        diff.append((n2 % 10 - n % 10))
        price.append(n2 % 10)
        n = n2
    res += n
    prices.append(price)
    diffs.append(diff)

print(f"Part 1: {res}")
# %%

sequences = {}
for d in range(len(diffs)):
    for i in range(len(diffs[d]) - 3):
        sequence = tuple(diffs[d][i : i + 4])
        if sequence in sequences:
            if d not in sequences[sequence]:
                sequences[sequence][d] = prices[d][i + 3]
        else:
            sequences[sequence] = {d: prices[d][i + 3]}

banana_max = 0
sequence_max = ()
for sequence, p in sequences.items():
    if sum(list(p.values())) > banana_max:
        banana_max = sum(list(p.values()))
        sequence_max = sequence

print(f"Part 2: {sequence_max} gives {banana_max} bananas")
# %%
