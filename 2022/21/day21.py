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
        print(monkeys)
    print(call_monkey(monkeys, "root"))  # 81075092088442


if __name__ == "__main__":
    main()
