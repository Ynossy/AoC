# %%
with open("input.txt") as f:
    boxes = [[int(x) for x in line.split(",")] for line in f.read().strip().split()]
# %%
distances = []
for i in range(len(boxes) - 1):
    for j in range(i + 1, len(boxes)):
        d = (
            (boxes[i][0] - boxes[j][0]) ** 2
            + (boxes[i][1] - boxes[j][1]) ** 2
            + (boxes[i][2] - boxes[j][2]) ** 2
        )
        distances.append([(i, j), d])

distances.sort(key=lambda x: x[1])


def addConnection(connections, box):
    in0 = -1
    in1 = -1
    for c in range(len(connections)):
        if box[0] in connections[c]:
            in0 = c
        if box[1] in connections[c]:
            in1 = c
    if in0 == in1 == -1:
        connections.append([*box])
    elif in0 == in1:
        return
    elif in0 != -1 and in1 != -1:
        connections[in0] += connections[in1]
        connections.pop(in1)
    elif in0 != -1:
        connections[in0].append(box[1])
    elif in1 != -1:
        connections[in1].append(box[0])


# %%
connections = []
for box, _ in distances[:1000]:
    addConnection(connections, box)

lens = [len(c) for c in connections]
lens.sort(reverse=True)
print(f"Part 1: {lens[0]*lens[1]*lens[2]}")  # 123234
# %%
connections = []
result = 0
for box, _ in distances:
    addConnection(connections, box)
    if len(connections[0]) == len(boxes):
        result = boxes[box[0]][0] * boxes[box[1]][0]
        break

print(f"Part 2: {result}")  # 9259958565
# %%
