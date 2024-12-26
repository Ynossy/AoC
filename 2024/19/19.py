# %%
with open("input.txt") as f:
    patterns, designs = f.read().strip().split("\n\n")
    patterns = patterns.strip().split(", ")
    designs = designs.strip().splitlines()


class TreeNode:
    def __init__(self, leaf: bool):
        self.leaf = leaf
        self.children = {}

    def __repr__(self):
        return f"leaf: {self.leaf}, children: {self.children}"

    def __str__(self):
        return f"leaf: {self.leaf}, children: {self.children}"


patternTree = TreeNode(False)


def insertPattern(node: TreeNode, pattern):
    isLeaf = len(pattern) == 1
    if pattern[0] not in node.children:
        node.children[pattern[0]] = TreeNode(isLeaf)
        if not isLeaf:
            insertPattern(node.children[pattern[0]], pattern[1:])
    elif isLeaf:
        node.children[pattern[0]].leaf = True
    else:
        insertPattern(node.children[pattern[0]], pattern[1:])


def checkDesign(design, idx, cache):
    if cache[idx] == 1:
        return True
    if cache[idx] == 2:
        return False
    node = patternTree
    i = idx
    while i < len(design) and design[i] in node.children:
        if node.children[design[i]].leaf:
            if i == len(design) - 1:
                cache[idx] = 1
                return True
            elif i + 1 < len(design) and checkDesign(design, i + 1, cache):
                cache[idx] = 1
                return True
        node = node.children[design[i]]
        i += 1
    cache[idx] = 2
    return False


for pattern in patterns:
    insertPattern(patternTree, pattern)


res = 0
for design in designs:
    if checkDesign(design, 0, [0 for _ in range(len(design))]):
        res += 1
print(f"Part 1: {res}")


# %%
