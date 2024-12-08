# %%
with open("example.txt") as f:
    data = [x.strip() for x in f.readlines()]
    antennas = {}
    dim_x = len(data)
    dim_y = len(data[0])
    for x in range(dim_x):
        for y in range(dim_y):
            if data[x][y] == ".":
                continue
            if data[x][y] in antennas:
                antennas[data[x][y]].append((x, y))
            else:
                antennas[data[x][y]] = [(x, y)]


# %%
def countAntinodes(part2=False):
    antinodes = set()
    for antenna in antennas:
        for a in antennas[antenna]:
            for b in antennas[antenna]:
                if a == b:
                    continue
                dx = a[0] - b[0]
                dy = a[1] - b[1]
                a_x = b[0] + dx if part2 else a[0] + dx
                a_y = b[1] + dy if part2 else a[1] + dy
                while 0 <= a_x < dim_x and 0 <= a_y < dim_y:
                    antinodes.add((a_x, a_y))
                    if not part2:
                        break
                    a_x += dx
                    a_y += dy

    return len(antinodes)


print(f"Part 1: {countAntinodes()}")
print(f"Part 2: {countAntinodes(part2=True)}")
# %%
