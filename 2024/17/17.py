# %%
with open("input.txt") as f:
    reg, ops = f.read().strip().split("\n\n")
    reg = [int(x.split(": ")[-1]) for x in reg.split("\n")]
    ops = [int(x) for x in ops.split(": ")[-1].split(",")]

output = []


def combo(x):
    if 0 <= x <= 3:
        return x
    elif x == 4:
        return reg[0]
    elif x == 5:
        return reg[1]
    elif x == 6:
        return reg[2]
    print(f"Illegal operation: {x}")
    return None


def instruction(instruction_pointer, opcode, operand):
    if opcode == 0:  # adv
        reg[0] = reg[0] // 2 ** combo(operand)
    elif opcode == 1:
        reg[1] = reg[1] ^ operand
    elif opcode == 2:
        reg[1] = combo(operand) % 8
    elif opcode == 3:
        if reg[0] > 0:
            instruction_pointer = operand
            return instruction_pointer
    elif opcode == 4:
        reg[1] = reg[1] ^ reg[2]
    elif opcode == 5:
        output.append(combo(operand) % 8)
    elif opcode == 6:
        reg[1] = reg[0] // 2 ** combo(operand)
    elif opcode == 7:
        reg[2] = reg[0] // 2 ** combo(operand)

    instruction_pointer += 2
    return instruction_pointer


instruction_pointer = 0
while instruction_pointer < len(ops):
    instruction_pointer = instruction(
        instruction_pointer, ops[instruction_pointer], ops[instruction_pointer + 1]
    )

print(f"Part1: {','.join([str(x) for x in output])}")

# %%
