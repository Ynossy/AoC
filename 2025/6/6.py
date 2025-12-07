# %%

with open("input.txt") as f:
    data_p2 = f.read().strip().split("\n")
    data = [x.split() for x in data_p2]

# %%

result = 0

for n, op in enumerate(data[-1]):
    if op == "+":
        calc = sum(int(x[n]) for x in data[:-1])
    elif op == "*":
        calc = 1
        for x in data[:-1]:
            calc *= int(x[n])
    result += calc

print(f"Part 1: {result}")  # 7229350537438
# %%

result = 0

operators = data[-1].copy()
op = operators.pop(0)
calculation = 1 if op == "*" else 0
for i in range(len(data_p2[0])):
    number = 0
    empty = True
    for row in data_p2[:-1]:
        if row[i] != " ":
            number = number * 10 + int(row[i])
            empty = False
    if empty:
        result += calculation
        op = operators.pop(0)
        calculation = 1 if op == "*" else 0
    elif op == "*":
        calculation *= number
    elif op == "+":
        calculation += number
result += calculation # last result does not trigger empty == True

print(f"Part 2: {result}")  # 11479269003550
# %%
