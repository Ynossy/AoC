#%% 
with open("input.txt") as f:
    reports = [[int(y) for y in x.strip().split(" ")] for x in f.readlines()]
# %%

def check_report(report):
    diff = [report[i+1] - report[i] for i in range(len(report)-1)]
    increasing = all(x>0 for x in diff)
    decreasing = all(x<0 for x in diff)

    levels = all(abs(x) <= 3 for x in diff)
    return (increasing or decreasing) and levels
    
safe_reports = sum(check_report(report) for report in reports)

print(f"Part 1: {safe_reports}")
# %%
count = 0

for report in reports:
    diff = [report[i+1] - report[i] for i in range(len(report)-1)]
    increasing = sum(x>0 for x in diff)
    decreasing = sum(x<0 for x in diff)
    sign = 1 if increasing > decreasing else -1
    safe = True
    for i in range(len(diff)):
        if sign*diff[i] <= 0 or sign*diff[i] > 3:
            safe = False
            break
    # remove first potential issue
    list_v1 = report.copy()
    list_v1.pop(i)
    # remove second potential issue
    list_v2 = report.copy()
    list_v2.pop(i+1)

    if safe or check_report(list_v1) or check_report(list_v2):
        count += 1

print(f"Part 2: {count}")
# %%
