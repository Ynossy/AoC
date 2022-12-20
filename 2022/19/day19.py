
def simulate(blueprint, t):
    res = [0, 0 ,0, 0] # ore clay obsidian
    robots = [1, 0, 0, 0] #ore clay obs geode
    for i in range(t):
        new_robots = [0,0,0,0]
        if res[2] >= blueprint[5] and res[0] >= blueprint[4]:
            new_robots[3] += 1
            res[3] -= blueprint[5]
            res[0] -= blueprint[4]
        if res[1] >= blueprint[3] and res[0] >= blueprint[2]:
            new_robots[2] += 1
            res[2] -= blueprint[3]
            res[0] -= blueprint[2]
        if res[0] >= blueprint[1]:
            new_robots[1] += 1
            res[0] -= blueprint[1]
        if res[0] >= blueprint[0]:
            new_robots[0] += 1
            res[0] -= blueprint[0]
        
        res = [res[i]+robots[i] for i in range(4)]
        robots = [new_robots[i]+robots[i] for i in range(4)]
        print(robots, res)
        



def main():
    with open("example.txt") as f:
        blueprints = [
            [
                int(line.split(" ")[6]),
                int(line.split(" ")[12]),
                int(line.split(" ")[18]),
                int(line.split(" ")[21]),
                int(line.split(" ")[27]),
                int(line.split(" ")[30]),
            ]
            for line in f.read().strip().split("\n") # ore-robot, clay-robot, obsidian-r-ore, obsidian-r-clay, geode-r-ore, geode-r-clay
        ]

    geode = simulate(blueprints[0], 24)

if __name__ == "__main__":
    main()
