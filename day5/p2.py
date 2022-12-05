import re
with open('input.txt') as f:
    lines = [x.rstrip() for x in f]

idxs = []
stacks = [[], [], [], [], [], [], [], [], []]
for i in reversed(range(0, 9)):
    if i == 8:
        for i, x in enumerate(lines[i]):
            if x.isnumeric():
                idxs.append(i)
    else:
        for a in idxs:
            try:
                if lines[i][a].isalpha():
                    if a == 1:
                        stacks[0].append(lines[i][a])
                    if a == 5:
                        stacks[1].append(lines[i][a])
                    if a == 9:
                        stacks[2].append(lines[i][a])
                    if a == 13:
                        stacks[3].append(lines[i][a])
                    if a == 17:
                        stacks[4].append(lines[i][a])
                    if a == 21:
                        stacks[5].append(lines[i][a])
                    if a == 25:
                        stacks[6].append(lines[i][a])
                    if a == 29:
                        stacks[7].append(lines[i][a])
                    if a == 33:
                        stacks[8].append(lines[i][a])
            except:
                pass

for line in lines[10:]:
    splt = re.split('move |from |to ', line)
    move_how_many, from_where, to_where = int(splt[1]), int(splt[2]) - 1, int(splt[3]) - 1
    tmp_stack = []
    for i in range(move_how_many):
        if len(stacks[from_where]) > 0:
            tmp_stack.append(stacks[from_where].pop())
    for i in reversed(range(len(tmp_stack))):
        stacks[to_where].append(tmp_stack[i])

ans = ''
for stack in stacks:
    ans += stack[len(stack) - 1]

print(ans)