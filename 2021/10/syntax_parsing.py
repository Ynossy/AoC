#%%

# with open("example.txt") as f:
with open("input.txt") as f:
    lines = f.readlines()

lines = [x.strip() for x in lines]


def parse_brackets(string):
    stack = []
    for s in string:
        if s in ["[", "(", "<", "{"]:
            stack.append(s)
        else:
            opening = stack.pop()
            if (
                opening == "["
                and s == "]"
                or opening == "("
                and s == ")"
                or opening == "<"
                and s == ">"
                or opening == "{"
                and s == "}"
            ):
                continue
            else:
                return s, stack
    return None, stack


def score(s):
    # Score  the illegal CLOSING character
    points = {"]": 57, ")": 3, ">": 25137, "}": 1197}
    return points[s]


def score_missing(stack):
    # score the remaining OPENING characters on the Stack
    score = 0
    points = {"[": 2, "(": 1, "<": 4, "{": 3}
    while stack:
        score *= 5
        c = stack.pop()
        score += points[c]
    return score


syntax_score = 0
completing_score = []
for line in lines:
    missing_bracket, closing = parse_brackets(line)
    if missing_bracket:
        syntax_score += score(missing_bracket)
    else:
        completing_score.append(score_missing(closing))

# Part 1
print(f"Syntax Error Score: {syntax_score}")

# Part 2
completing_score.sort()
print(f"completing Score: {completing_score[len(completing_score)//2]}")

# %%
