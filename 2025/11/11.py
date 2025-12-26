# %%
with open("input.txt") as f:
    graph = {
        line.split(": ")[0]: line.split(": ")[1].split(" ")
        for line in f.read().strip().split("\n")
    }
# %%
result = 0
nodes = ["you"]
while nodes:
    node = nodes.pop()
    if node == "out":
        result += 1
    else:
        for n in graph[node]:
            nodes.append(n)
print(f"Part 1: {result}")  # 599

# %%
lookup = {}


def countPaths(node):
    if node[0] == "out":
        return node[1] == True and node[2] == True

    fft = True if node[0] == "fft" else node[1]
    dac = True if node[0] == "dac" else node[2]

    path_count = 0
    for n in graph[node[0]]:
        new_node = (n, fft, dac)
        if new_node in lookup:
            path_count += lookup[new_node]
        else:
            p = countPaths(new_node)
            lookup[new_node] = p
            path_count += p
    return path_count


print(f"Part 2: {countPaths((('svr', False, False)))}")  # 393474305030400
# %%
