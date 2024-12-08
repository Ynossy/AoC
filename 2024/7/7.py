# %%

with open("input.txt") as f:
    data = f.readlines()
    operations = []
    for operation in data:
        solution, operands = operation.split(": ")
        operations.append([int(solution), [int(x) for x in operands.split(" ")]])
# %%
operators = [lambda a, b: a * b, lambda a, b: a + b, lambda a, b: int(f"{a}{b}")]


def op(_result, _current, _operands, _opIdx, part2=False):
    if len(_operands) == 1:
        return operators[_opIdx](_current, _operands[0]) == _result
    _current = operators[_opIdx](_current, _operands[0])
    if _current > _result:
        return False
    return (
        op(_result, _current, _operands[1:], 0, part2)
        or op(_result, _current, _operands[1:], 1, part2)
        or part2
        and op(_result, _current, _operands[1:], 2, part2)
    )


res = sum(
    operation[0] for operation in operations if op(operation[0], 0, operation[1], 1)
)
print(f"Part 1: {res}")
res = sum(
    operation[0]
    for operation in operations
    if op(operation[0], 0, operation[1], 1, part2=True)
)
print(f"Part 2: {res}")
# %%
