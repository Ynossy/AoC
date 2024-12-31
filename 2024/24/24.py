# %%
with open("input.txt") as f:
    values, data = f.read().strip().split("\n\n")
    values = {x.split(": ")[0]: int(x.split(": ")[1]) for x in values.splitlines()}
    gates = {}
    for gate in data.splitlines():
        logic, result = gate.split(" -> ")
        gates[result] = logic.split(" ")

operators = {
    "XOR": lambda l, r: l ^ r,
    "OR": lambda l, r: l | r,
    "AND": lambda l, r: l & r,
}


def calculate(output):
    if output in values:
        return values[output]
    left, operator, right = gates[output]
    if left not in values:
        calculate(left)
    if right not in values:
        calculate(right)
    res = operators[operator](values[left], values[right])

    values[output] = res
    return res


for output in gates:
    calculate(output)

results = [[x, values[x]] for x in values]
results.sort(key=lambda x: x[0])
output_binary = ""
for x in results:
    if x[0][0] == "z":
        output_binary = str(x[1]) + output_binary
print(f"Part 1: {int(output_binary, base=2)}")
