#%%
"""

NOT WORKING

probably needs a shortest path finding algorithm 
to go through all possible combinations of moves



"""
with open("input.txt") as f:
    codes = f.read().strip().split("\n")

def vectorToInstructionsNum(dx, dy, reorder1, reorder2):
    instructions = ""
    if reorder1 and dx < 0:
        instructions += abs(dx)*"<"
        dx = 0
    if reorder2 and dy > 0:
        instructions += abs(dy)*"v"
        dy = 0
    if dx > 0:
        instructions += abs(dx)*">"
    if dy > 0:
        instructions += abs(dy)*"v"
    if dy < 0:
        instructions += abs(dy)*"^"
    if dx < 0:
        instructions += abs(dx)*"<"
    return instructions

def vectorToInstructionsDir(dx, dy):
    instructions = ""
    if dx > 0:
        instructions += abs(dx)*">"
    if dy < 0:
        instructions += abs(dy)*"^"
    if dy > 0:
        instructions += abs(dy)*"v"
    if dx < 0:
        instructions += abs(dx)*"<"
    return instructions
    
# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+
numKeys = {"7":(0,0), "8":(1,0), "9":(2,0), 
        "4":(0,1), "5":(1,1), "6":(2,1),
        "1":(0,2), "2":(1,2), "3":(2,2),
                    "0":(1,3), "A":(2,3)}
#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+
dirKeys = {           "^":(1,0), "A":(2,0), 
            "<":(0,1), "v":(1,1), ">":(2,1)}

def generateInput(numeric, input):
    keys = numKeys if numeric else dirKeys
    pos = "A"
    instructions = ""
    for c in input:
        dx = keys[c][0]-keys[pos][0]
        dy = keys[c][1]-keys[pos][1]
        if numeric:
            instructions += vectorToInstructionsNum(dx,dy, keys[pos][1]<=2, keys[c][1]<=2 or keys[c][0]>=1) + "A"
        else:    
            instructions += vectorToInstructionsDir(dx,dy) + "A"
        pos = c
    return instructions


# c1 = generateInput(True,"379A")
# c2 = generateInput(False, c1)
# c3 = generateInput(False, c2)
# print(len(c1), c1)
# print(len(c2), c2)
# print(len(c3), c3)
res = 0
for code in codes:
    c1 = generateInput(True, code)
    c2 = generateInput(False, c1)
    c3 = generateInput(False, c2)

    n = int(code[:-1])
    print(len(c3), n, c3)
    res += n * len(c3)

print(f"Part 1: {res}") 
# 172712 too high
# 166132 too low