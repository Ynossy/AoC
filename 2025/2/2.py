
#%% 

with open("input.txt") as f:
    data = [[int(y) for y in x.split("-")] for x in f.readline().strip().split(",")]

#%% part1
def checkRepetition(num_int: int):
    num = str(num_int)
    return num[:len(num)//2] == num[len(num)//2:]

result = 0
for x,y in data:
    for i in range(x,y+1):
        if checkRepetition(i):
            result += i
print(f"Part1: {result}") # 54641809925
    
# %% part 2

def checkRepetitionMulti(num_int: int):
    num = str(num_int)
    for i in range(2,len(num)+1):
        if len(num) % i != 0:
            continue
        l = len(num)//i
        values = []
        for x in range(i-1):
            a = num[l*x:l*(x+1)]
            b = num[l*(x+1):l*(x+2)]
            values.append(a==b)
        if all(values):
            return True
    return False

result = 0
for x,y in data:
    for i in range(x,y+1):
        if checkRepetitionMulti(i):
            result += i
print(f"Part2: {result}") # 73694270688

# %%
