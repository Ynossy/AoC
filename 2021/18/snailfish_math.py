#%%
from time import perf_counter


def explode(lst, d):
    if d == 4 and isinstance(lst, list):
        # return abort flag and explodable values
        return True, lst[0], lst[1]

    b = False
    r = None
    l = None
    if isinstance(lst[0], list):
        # left branch
        b, l, r = explode(lst[0], d + 1)
        if b and d == 3:
            lst[0] = 0
        if b and r:
            if not isinstance(lst[1], list):
                lst[1] += r
            else:
                # go one right, then only left
                insert(lst[1], r, 0)
            return b, l, None
    if not b and isinstance(lst[1], list):
        # right branch
        b, l, r = explode(lst[1], d + 1)
        if b and d == 3:
            lst[1] = 0
        if b and l:
            if not isinstance(lst[0], list):
                lst[0] += l
            else:
                # go one left, then only right
                insert(lst[0], l, 1)
            return b, None, r
    # pass remaining stuff to parent node
    return b, l, r


def split(lst):
    # returns true for aborting when a single value was split
    for i in range(2):
        if isinstance(lst[i], list):
            if split(lst[i]):
                return True
        elif lst[i] > 9:
            lst[i] = [lst[i] // 2, (lst[i] + 1) // 2]
            return True


def insert(lst, value, dir):
    # 0 for left, 1 for right
    while isinstance(lst[dir], list):
        lst = lst[dir]
    lst[dir] += value


def simplify(expression):
    while explode(expression, 0)[0] or split(expression):
        pass
    return expression


def magnitude(lst):
    if isinstance(lst, int):
        return lst
    return 3 * magnitude(lst[0]) + 2 * magnitude(lst[1])


# ------------------- Main Evaluation -----------------
start = perf_counter()

with open("input.txt") as f:
    input = f.readlines()

lst = eval(input[0])
for i in input[1:]:
    lst = simplify([lst, eval(i)])

print(f"Magnitude Result: {magnitude(lst)}")
print(f"Runtime: {perf_counter()-start}")

# %% part 2 - just bruteforce all of them
start = perf_counter()
max = 0
snailfish_numbers = [eval(x) for x in input]
for i in snailfish_numbers:
    for j in snailfish_numbers:
        t = magnitude(simplify([i, j]))
        if t > max:
            max = t

print(f"Maximal Snailfish sum: {max}")
print(f"Runtime: {perf_counter()-start}")
