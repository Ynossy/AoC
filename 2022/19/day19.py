import time

idx = {"ore": 0, "clay": 1, "obsidian": 2, "geode": 3}


def ceil(a):
    b = int(a)
    return b + int(b < a)


def search(bp, robots, res, t, next_robot):
    if t <= 0:
        return res[idx["geode"]] + t * robots[idx["geode"]]
    if next_robot == "ore":
        res[0] -= bp[0]
    elif next_robot == "clay":
        res[0] -= bp[1]
    elif next_robot == "obsidian":
        res[0] -= bp[2]
        res[1] -= bp[3]
    elif next_robot == "geode":
        res[0] -= bp[4]
        res[2] -= bp[5]
    res = [a + b for a, b in zip(res, robots)]
    next_states = []
    for nr in ["geode", "obsidian", "clay", "ore"]:
        if (nr == "ore" and robots[idx["ore"]] > bp[0]) or (
            nr == "clay" and robots[idx["clay"]] > bp[3]
        ):
            continue
        robots_p1 = robots.copy()
        if next_robot:
            robots_p1[idx[next_robot]] += 1
        if nr == "ore":
            dt = max(0, ceil((bp[0] - res[idx["ore"]]) / robots_p1[idx["ore"]]))
        elif nr == "clay":
            dt = max(0, ceil((bp[1] - res[idx["ore"]]) / robots_p1[idx["ore"]]))
        elif nr == "obsidian" and robots_p1[idx["clay"]] > 0:
            dt = max(
                0,
                ceil((bp[2] - res[idx["ore"]]) / robots_p1[idx["ore"]]),
                ceil((bp[3] - res[idx["clay"]]) / robots_p1[idx["clay"]]),
            )
        elif nr == "geode" and robots_p1[idx["obsidian"]] > 0:
            dt = max(
                0,
                ceil((bp[4] - res[idx["ore"]]) / robots_p1[idx["ore"]]),
                ceil((bp[5] - res[idx["obsidian"]]) / robots_p1[idx["obsidian"]]),
            )
        else:
            continue
        res_p1 = [a + min(dt, t) * b for a, b in zip(res, robots_p1)]
        next_states.append(search(bp, robots_p1, res_p1, t - dt - 1, nr))

        if (nr == "obsidian" or nr == "geode") and dt == 0:
            # skip clay and ore branches once we can always build obsidians or geode (geode higher prio)
            break

    return max(next_states)


def main():
    with open("input.txt") as f:
        blueprints = [
            [
                int(line.split(" ")[6]),
                int(line.split(" ")[12]),
                int(line.split(" ")[18]),
                int(line.split(" ")[21]),
                int(line.split(" ")[27]),
                int(line.split(" ")[30]),
            ]
            for line in f.read()
            .strip()
            .split(
                "\n"
            )  # ore-robot, clay-robot, obsidian-r-ore, obsidian-r-clay, geode-r-ore, geode-r-obsidian
        ]

    robots = [1, 0, 0, 0]
    res = [0, 0, 0, 0]

    t0 = time.time()
    r = 0
    for i, bp in enumerate(blueprints):
        p = search(blueprints[i], robots, res, 24, None)
        r += (i + 1) * p
        print(i + 1, p)
    print(f"Result 1: {r}")  # Part1: 1147
    print(f"Runtime: {time.time()-t0}")  # 4.0s

    t0 = time.time()
    r2 = []
    for i in range(3):
        r2.append(search(blueprints[i], robots, res, 32, None))
        print(i + 1, r2[-1])
    print(f"Result 2: {r2[0]*r2[1]*r2[2]}")  # Part2: 3080
    print(f"Runtime: {time.time()-t0}")  # 15.1s


if __name__ == "__main__":
    main()
