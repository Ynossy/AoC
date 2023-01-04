idx = {"ore": 0, "clay": 1, "obsidian": 2, "geode": 3}


def ceil(a):
    b = int(a)
    return b + int(b<a)


def search(bp, robots, res, t, next_robot):
    # print(robots, res)
    assert all([x >= 0 for x in res]), res
    if t == 0:
        return res[idx["geode"]]
    elif t<0:
        return res[idx["geode"]] +t* robots[idx["geode"]]
    if next_robot == "ore":
        assert res[0] >= bp[0], res
        res[0] -= bp[0]
    elif next_robot == "clay":
        assert res[0] >= bp[1], res
        res[0] -= bp[1]
    elif next_robot == "obsidian":
        assert res[0] >= bp[2], res
        res[0] -= bp[2]
        assert res[1] >= bp[3], res
        res[1] -= bp[3]
    elif next_robot == "geode":
        assert res[0] >= bp[4], res
        res[0] -= bp[4]
        assert res[2] >= bp[5], res
        res[2] -= bp[5]
    res = [a + b for a, b in zip(res, robots)]
    next_states = []
    # print(robots)
    for nr in idx.keys():
        if nr in ["ore", "clay"] and robots[idx[nr]] > 4:
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

    return max(next_states)


def main():
    with open("19/example.txt") as f:
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
    p1 = search(blueprints[1], robots, res, 24, None)
    print(f"Result: {p1}")


if __name__ == "__main__":
    main()
