import time

def find_shortest_path(rooms, start, end):  # BFS
    stack = [start]
    dist = {name: 1000 for name in rooms.keys()}
    dist[start] = 0
    while stack:
        current = stack.pop(0)
        if current == end:
            return dist[current]
        for neighbor in rooms[current][1]:
            if dist[neighbor] > dist[current] + 1:
                dist[neighbor] = dist[current] + 1
                stack.append(neighbor)
    return -1


def maximal_pressure(room, t, rooms, good_valves, path_len, open_valves):
    rate = sum([rooms[r][0] for r in good_valves if open_valves[r]])
    # print(room, rate, t)
    if sum([x for x in open_valves.values()]) == len(good_valves):
        return rate * t
    J = []
    for next_valve in good_valves:
        if open_valves[next_valve]==True:
            continue
        o = open_valves.copy()
        o[next_valve] = True
        if t - path_len[room][next_valve] - 1 > 0:
            J.append(
                rate * (path_len[room][next_valve] + 1)
                + maximal_pressure(
                    next_valve,
                    t - path_len[room][next_valve] - 1,
                    rooms,
                    good_valves,
                    path_len,
                    o,
                )
            )
    J.append(rate * t)
    # print(J)
    return max(J)


def main():
    t0 = time.time()
    with open("input.txt") as f:
        rooms = {
            s.split(" ")[1]: [
                int(s.split(" ")[4].split("=")[1][:-1]),
                [v[:-1] if len(v) == 3 else v for v in s.split(" ")[9:]],
            ]
            for s in f.read().strip().split("\n")
        }
    opened = {r: rooms[r][0] == 0 for r in rooms.keys()}
    good_valves = [r for r, v in rooms.items() if v[0] > 0]
    good_valves.append("AA")
    print(good_valves)
    path_len = {
        b: {a: find_shortest_path(rooms, a, b) for a in good_valves}
        for b in good_valves
    }
    open_valves = {name: False for name in good_valves}
    open_valves["AA"] = True
    print(maximal_pressure("AA", 30, rooms, good_valves, path_len, open_valves)) #1845 right
    t1 = time.time()
    print(f"Time Part 1: {t1-t0:.3}s")


if __name__ == "__main__":
    main()
