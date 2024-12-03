#%%

with open("input.txt") as f:
    data = f.read().strip()
# %%

def findNumber(inst):
    if not inst[0].isnumeric():
        return -1
    if not inst[1].isnumeric():
        return 1
    if not inst[2].isnumeric():
        return 2
    return 3

def scanInstructions(instructions, part2=False):
    result = 0
    i = 0
    do = True
    while i<len(instructions):
        instrDo = instructions.find("do()", i)
        instrDont = instructions.find("don't()", i)
        start = instructions.find("mul(", i)
        if start == -1:
            break
        if instrDo != -1 and instrDo < start and (instrDont < instrDo or start < instrDont):
            do = True
        if instrDont != -1 and instrDont < start and (instrDo < instrDont or start < instrDo):
            do = False
        i = start + 4 
        ptr_n1 = findNumber(instructions[i:])
        if ptr_n1 == -1:
            continue
        n1 = int(instructions[i:i+ptr_n1])
        i += ptr_n1
        if instructions[i] != ',':
            continue
        i += 1
        ptr_n2 = findNumber(instructions[i:])
        if ptr_n2 == -1:
            continue
        n2 = int(instructions[i:i+ptr_n2])
        i += ptr_n2
        if instructions[i] != ')':
            continue
        if not part2 or do:
            result += n1*n2
    return result

print(f"Part 1: {scanInstructions(data)}")
print(f"Part 1: {scanInstructions(data, True)}") # 113204715 too high
# %%
