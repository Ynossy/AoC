operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}


def call_monkey(monkeys, name):
    operation = monkeys[name]
    if operation.isnumeric():
        return int(operation)
    return operations[operation[5]](
        call_monkey(monkeys, operation[:4]), call_monkey(monkeys, operation[-4:])
    )


def main():
    with open("input.txt") as f:
        monkeys = {
            s.split(": ")[0]: s.split(": ")[1] for s in f.read().strip().split("\n")
        }
        # print(monkeys)
    print(f"Part 1: {int(call_monkey(monkeys, 'root'))}")  # 81075092088442

    n = 1
    for i in range(100):
        monkeys["humn"] = f"{n}"
        a1 = call_monkey(monkeys, monkeys["root"][:4])
        b1 = call_monkey(monkeys, monkeys["root"][-4:])
        monkeys["humn"] = f"{n+100}"
        a2 = call_monkey(monkeys, monkeys["root"][:4])
        b2 = call_monkey(monkeys, monkeys["root"][-4:])

        n = int(n - (a1 - b1) / ((a2 - b2) - (a1 - b1)) * 100)  # Newton step
        if a1 == b1:
            print(f"Part 2: {n} | found in {i} Newton steps")  # 3349136384441
            break


if __name__ == "__main__":
    main()
