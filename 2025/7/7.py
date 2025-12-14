# %%

with open("input.txt") as f:
    data = [list(row) for row in f.read().strip().split("\n")]

# %%

lasers = {}
# start point
for i in range(len(data[0])):
    if data[0][i] == "S":
        lasers[1, i] = 1  # timelines
        break

# simulate lasers
total_timelines = 0
splitters_hit = 0
while lasers:
    new_lasers = {}

    def add_laser(x, y, t):
        if (x, y) in new_lasers:
            new_lasers[(x, y)] += t
        else:
            new_lasers[(x, y)] = t

    for (laser_x, laser_y), timelines in lasers.items():
        if laser_x + 1 >= len(data):
            total_timelines += timelines
        elif data[laser_x + 1][laser_y] == ".":
            add_laser(laser_x + 1, laser_y, timelines)
        elif data[laser_x + 1][laser_y] == "^":
            splitters_hit += 1
            add_laser(laser_x + 1, laser_y + 1, timelines)
            add_laser(laser_x + 1, laser_y - 1, timelines)

    lasers = new_lasers

print(f"Part1: {splitters_hit}")  # 1656
print(f"Part2: {total_timelines}")  # 76624086587804
