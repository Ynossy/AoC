#%%
with open("input.txt") as f:
    buyers = [int(x) for x in f.readlines()]


def nextRng(num):
    num = ((num*64) ^ num) % 16777216
    num = ((num//32) ^num ) % 16777216
    num = ((num*2048) ^num) % 16777216
    return num

res = 0
for b in buyers:
    n = b
    for _ in range(2000):
        n = nextRng(n)
    res += n

print(f"Part 1: {res}")