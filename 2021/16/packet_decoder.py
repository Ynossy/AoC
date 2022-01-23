#%%

with open("input.txt") as f:
    input = f.readline().strip()

# examples:
# input = "D2FE28" #literal 2021
# input = "38006F45291200"  # operator 0, 2 subliterals
# input = "EE00D40C823060"  # operator 1, 3 subliterals
# input = "8A004A801A8002F478"  # version sum 16
# input = "620080001611562C8802118E34"  # 2*2 literals, version sum 12
# input = "C0015000016115A2E0802F182340"  # 2*2 literals, version sum 23
# input = "A0016C880162017C3686B18A3D4780"  # 5 literals, version sum 31

# input = "C200B40A82"  # sum 1+2
# input = "04005AC33890"  # 6*9
# input = "9C0141080250320F1802104A08"  # 1+3 == 2*2
# input = "880086C3E88112"  # min(7,8,9)
# input = "CE00C43D881120"  # max(7,8,9)
# input = "D8005AC2A8F0"  # 5<15
# input = "F600BC2D8F"  # 5!<15
# input = "9C005AC2F8F0"  # 5!=15

binary = format(int(input, 16), "0" + str(len(input) * 4) + "b")

# %% part 2
import numpy as np
from time import perf_counter

start = perf_counter()

version_sum = 0


def packet(s):
    global version_sum
    version_sum += int(s[:3], 2)
    id = int(s[3:6], 2)
    
    num, idx = literal(s[6:]) if id == 4 else operator(id, s[6:])
    # print(f"Packet ID: {id}, Packet Result: {num}")
    return num, 6 + idx


def literal(s):
    idx = 0
    payload = ""
    while s[idx] == "1":
        payload += s[idx + 1 : idx + 5]
        idx += 5
    payload += s[idx + 1 : idx + 5]
    idx += 5
    # print(f"Literal Payload: {int(payload,2)}")
    return int(payload, 2), idx


def operator(id, s):
    vals = []
    if s[0] == "0":
        idx = int(s[1 : 1 + 15], 2) + 15 + 1
        sub = 16
        while sub < idx:
            n, i = packet(s[sub:idx])
            sub += i
            vals.append(n)
    else:
        idx = 11 + 1
        packet_count = int(s[1:idx], 2)
        for _ in range(packet_count):
            n, i = packet(s[idx:])
            idx += i
            vals.append(n)

    operators = [
        np.sum,
        lambda x: np.prod(x, dtype=np.float64),
        np.min,
        np.max,
        None,
        lambda x: int(x[0] > x[1]),
        lambda x: int(x[0] < x[1]),
        lambda x: int(x[0] == x[1]),
    ]
    num = operators[id](vals)
    return num, idx


num, _ = packet(binary)
print(f"Runtime: {perf_counter()-start}")
print(f"Version number sum: {version_sum}")
print(f"Packet Result: {num}")

# %%
