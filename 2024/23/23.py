# %%
connections = {}


def add_connection(p1, p2):
    if p1 in connections:
        connections[p1].add(p2)
    else:
        connections[p1] = {p2}


with open("input.txt") as f:
    data = f.read().strip().splitlines()
    for con in data:
        p1, p2 = con.split("-")
        add_connection(p1, p2)
        add_connection(p2, p1)

triplets = []

for pc1 in connections:
    for pc2 in connections[pc1]:
        for pc3 in connections[pc1].intersection(connections[pc2]):
            if pc1[0] == "t" or pc2[0] == "t" or pc3[0] == "t":
                triplets.append([pc1, pc2, pc3])

print(f"Part 1: {len(triplets)//6}")
