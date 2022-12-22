idx = {"ore": 0, "clay": 1, "obsidian": 2, "geode": 3}


def search(bp, robots, res, t, next_robot):
    if t <= 0:
        return res[idx["geode"]]
    next_states = []
    print(robots)

    for nr in idx.keys():
        if nr in ["ore", "clay"] and robots[idx[nr]]>4:
            continue
        robots_p1 = robots.copy()
        robots_p1[idx[next_robot]] += 1
        if nr == "ore":
            dt = max(
                1,
                (bp[0] - res[idx["ore"]] + robots[idx["ore"]] - 1)
                // robots[idx["ore"]],
            )
        elif nr == "clay":
            dt = max(
                1,
                (bp[1] - res[idx["ore"]] + robots[idx["ore"]] - 1)
                // robots[idx["ore"]],
            )
        elif nr == "obsidian" and robots[idx["clay"]]>0:
            dt = max(
                1,
                (bp[2] - res[idx["ore"]] + robots[idx["ore"]] - 1)
                // robots[idx["ore"]],
                (bp[3] - res[idx["clay"]] + robots[idx["clay"]] - 1)
                // robots[idx["clay"]],
            )
        elif nr == "geode" and robots[idx["obsidian"]]>0:
            dt = max(
                1,
                (bp[4] - res[idx["ore"]] + robots[idx["ore"]] - 1)
                // robots[idx["ore"]],
                (bp[5] - res[idx["obsidian"]] + robots[idx["obsidian"]] - 1)
                // robots[idx["obsidian"]],
            )
        else:
            dt = 1
        print(dt)
        res_p1 = [a + dt * b for a, b in zip(robots, res)]
        next_states.append(search(bp, robots_p1, res_p1, t - dt, nr))

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
    p1 = search(blueprints[0], robots, res, 24, "ore")
    print(p1)


if __name__ == "__main__":
    main()
