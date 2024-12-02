#%% 
with open("input.txt") as f:
    reports = [[int(y) for y in x.strip().split(" ")] for x in f.readlines()]
# %%

count = 0
diffs = [[report[i+1] - report[i] for i in range(len(report)-1)]for report in reports]
for report in diffs:
    increasing = all(x>0 for x in report)
    decreasing = all(x<0 for x in report)

    levels = all(abs(x) <= 3 for x in report)
    if (increasing or decreasing) and levels:
        count += 1
print(f"Part 1: {count}")
# %%
count = 0

for report in reports:
    diff = [report[i+1] - report[i] for i in range(len(report)-1)]
    increasing = sum(x>0 for x in diff)
    decreasing = sum(x<0 for x in diff)
    safe = True
    for i in range(len(diff)):
        if increasing > decreasing :
            if diff[i] <= 0 or diff[i] > 3:
                safe = False
                break
        else:
            if diff[i] >= 0 or diff[i] < -3:
                safe = False
                break
    if safe:
        count += 1
        continue
    
    list_v1 = report.copy()
    list_v1.pop(i)
    diff = [list_v1[i+1] - list_v1[i] for i in range(len(list_v1)-1)]
    increasing = all(x>0 for x in diff)
    decreasing = all(x<0 for x in diff)

    levels = all(abs(x) <= 3 for x in diff)
    if (increasing or decreasing) and levels:
        count += 1
        continue
    
    list_v2 = report.copy()
    list_v2.pop(i+1)
    diff = [list_v2[i+1] - list_v2[i] for i in range(len(list_v2)-1)]
    increasing = all(x>0 for x in diff)
    decreasing = all(x<0 for x in diff)

    levels = all(abs(x) <= 3 for x in diff)
    if (increasing or decreasing) and levels:
        count += 1
        continue

print(f"Part 2: {count}")

# %%
