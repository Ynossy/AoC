#%%

with open("input.txt") as f:
    groups = [s.strip().split("\n") for s in f.read().strip().split("\n\n")]
# %% part 1

questions = 0
for group in groups:
    q_set = set()
    for person in group:
        q_set.update(list(person))
    questions += len(q_set)

print(f"Part 1 - {questions}")

#%% part 2

questions = 0
for group in groups:
    q_set = set(list(group[0]))
    for person in group:
        q_set = q_set.intersection(list(person))
    questions += len(q_set)

print(f"Part 2 - {questions}")

# %%
