#%%

with open("input.txt") as f:
    data = f.readlines()
    operations = []
    for operation in data:
        solution, operands = operation.split(": ")
        operations.append([int(solution), [int(x) for x in operands.split(" ")]])
# %%
operators = [lambda a,b : a*b, lambda a,b : a+b, lambda a,b :int(str(a)+str(b))]

def op(_result, _current, _operands, _opIdx, part2 = False):
    if len(_operands) == 1:
        return operators[_opIdx](_current, _operands[0]) == _result
    if _current > _result:
        return False
    _current = operators[_opIdx](_current, _operands[0])
    if part2 and op(_result, _current, _operands[1:], 2, part2):
        return True
    if op(_result, _current, _operands[1:], 0, part2):
        return True
    return op(_result, _current, _operands[1:], 1, part2)

# for operation in operations:
#     print(f"{operation[0]}: {op(operation[0], 0, operation[1], 1, part2=True)}")

res = sum(operation[0] for operation in operations if op(operation[0], 0, operation[1], 1))
print(f"Part 1: {res}")
res = sum(operation[0] for operation in operations if op(operation[0], 0, operation[1], 1, part2=True))
print(f"Part 2: {res}")
# %%
