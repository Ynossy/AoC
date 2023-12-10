from copy import deepcopy


def run_monkeys(mk, mod, n, part):
    monkeys = deepcopy(mk)
    for _ in range(n):
        for m in monkeys:
            for i in range(len(m["items"])):
                m["inspect"] += 1
                old = m["items"].pop(0)
                if part == 1:
                    new = eval(m["op"]) % mod // 3
                else:
                    new = eval(m["op"]) % mod
                monkeys[m["throw"][new % m["test"] != 0]]["items"].append(new)
    print([m["inspect"] for m in monkeys])
    mb = sorted([m["inspect"] for m in monkeys])

    print(f"Monkeybusiness: {mb[-1]*mb[-2]}")


def main():
    with open("input.txt") as f:
        lines = f.readlines()
    monkeys = []
    mod = 1
    for i in range(len(lines) // 7 + 1):
        m = {}
        m["items"] = [int(x) for x in lines[i * 7 + 1].strip().split(":")[1].split(",")]
        m["op"] = lines[i * 7 + 2].strip().split(":")[1].split("= ")[-1]
        m["test"] = int(lines[i * 7 + 3].strip().split(" ")[-1])
        m["throw"] = [
            int(lines[i * 7 + 4].strip().split(" ")[-1]),
            int(lines[i * 7 + 5].strip().split(" ")[-1]),
        ]
        m["inspect"] = 0
        monkeys.append(m)
        mod *= m["test"]

    run_monkeys(monkeys, mod, 20, 1)  # 56120
    run_monkeys(monkeys, mod, 10000, 2)  # 24389045529


if __name__ == "__main__":
    main()
