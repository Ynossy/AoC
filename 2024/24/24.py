# %%
"""
DISCLAIMER:
Part 2 is mainly solved by hand and the code matches my result.
May not be complete for different inputs!
"""
with open("input.txt") as f:
    values, data = f.read().strip().split("\n\n")
    values = {x.split(": ")[0]: int(x.split(": ")[1]) for x in values.splitlines()}
    gates = {}
    gates_list = []  # result, left, operation, right
    for gate in data.splitlines():
        logic, result = gate.split(" -> ")
        gates[result] = logic.split(" ")
        gates_list.append([result, *gates[result]])

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

# %%
# Part 2: check the logic against the common full adder
# X1 XOR Y1 -> I1
# I1 XOR C0 -> Z1
# X1 AND Y1 -> I2
# I1 AND C0 -> I3
# I2 OR I3 -> C1

# Halfadder for X00 and Y00:
# X0 XOR Y0 -> Z00
# X0 AND Y1 -> C0


def find_gate(l, op, r):
    for g in gates_list:
        if g[2] == op and g[1] in [l, r] and g[3] in [l, r]:
            return g[0]
    return None


def find_missing(l, op):
    res = []
    for g in gates_list:
        if g[2] == op and g[1] == l:
            res.append(g[3])
        elif g[2] == op and g[3] == l:
            res.append(g[1])
    if len(res) == 1:
        return res[0]
    return None


bad_connections = set()
carries = [find_gate("x00", "AND", "y00")]

l0, op0, r0 = gates["z00"]
if not (l0 in ["x00", "y00"] and r0 in ["x00", "y00"] and op0 == "XOR"):
    print("Error in z00")
l0, op0, r0 = gates[carries[0]]
if not (l0 in ["x00", "y00"] and r0 in ["x00", "y00"] and op0 == "AND"):
    print("Error in c0")

for i in range(1, len(output_binary) - 1):
    i1 = find_gate(f"x{i:02}", "XOR", f"y{i:02}")
    i2 = find_gate(f"x{i:02}", "AND", f"y{i:02}")

    i1_check1 = find_missing(i1, "XOR")
    i1_check2 = find_missing(i1, "AND")
    if i1_check1 and i1_check1 == i1_check2:
        z = find_gate(i1, "XOR", carries[i - 1])
        if z != f"z{i:02}":
            print(f"{i}: Error in gate: {z}!= z{i:02}")
            if z:
                bad_connections.add(f"z{i:02}")
                bad_connections.add(z)
    else:
        print(f"{i}: missmatch for i1: {i1} vs {i1_check1}")
        bad_connections.add(i1)

    i2_check = find_missing(i2, "OR")
    if not i2_check:
        print(f"{i}: Error in first AND output")
        bad_connections.add(i2)

    i3 = find_gate(i1, "AND", carries[i - 1])
    if not i3:
        print(f"{i}: i3 not found: {i1, carries[i-1]}")
        c = find_gate(i2_check, "OR", i2)
        carries.append(c)
    else:
        c = find_gate(i2, "OR", i3)
        carries.append(c)

    next_i1 = find_gate(f"x{i+1:02}", "XOR", f"y{i+1:02}")
    c_in_1 = find_missing(next_i1, "XOR")
    c_in_2 = find_missing(next_i1, "AND")
    if c_in_1 and c_in_1 == c_in_2:
        if c != c_in_1:
            carries[i] = c_in_1
            if c:
                bad_connections.add(c)
                bad_connections.add(c_in_1)
            print(f"{i}: Fixed carry {c} -> {c_in_1}")

sorted_bad_connections = list(bad_connections)
sorted_bad_connections.sort()
print(f"Bad connections: {','.join(sorted_bad_connections)}")
# fcd,fhp,hmk,rvf,tpc,z16,z20,z33 correct! (by hand)
# %%
