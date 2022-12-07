from collections import defaultdict
from anytree import Node
with open('test.txt') as f:
    lines = [x.rstrip() for x in f]

EXEC = '$'
CD = 'cd'
LS = 'ls'
nodes = {}
current_dir = ''
dirs = set()
ls_mode = False
for line in lines:
    line = line.split(' ')
    if line[0] == EXEC or line[0] == CD:
            ls_mode = False
    if ls_mode:
        if line[0] == 'dir':
            nodes[current_dir][line[1]] = line[0]
            dirs.add(line[1])
        else:
            nodes[current_dir][line[0]] = line[1]
    last_dir = current_dir
    if line[0] == EXEC:
        if line[1] == CD:
            if line[2] == '..':
                current_dir = last_dir
            elif line[2] == '/':
                current_dir = line[2]
                dirs.add(current_dir)
                try:
                    nodes[line[2]]
                except:
                    nodes[line[2]] = {}
            else:
                if line[2] in nodes[current_dir]:
                    current_dir = line[2]
                    dirs.add(current_dir)
                    if nodes.get(line[2]) == None:
                        nodes[line[2]] = {}
        if line[1] == LS:
            ls_mode = True
#print(nodes)

folder_sizes = {}
for k in nodes:
    #first calculate all folder sizes
    for v in nodes[k]:
        if v.isnumeric():
            try:
                folder_sizes[k] += int(v)
            except:
                folder_sizes[k] = int(v)

for k in nodes:
    for v in nodes[k]:
        if v.isalpha():
            try:
                folder_sizes[k] += folder_sizes[v]
            except:
                pass

tot = 0
for k in folder_sizes:
    if folder_sizes[k] <= 100000:
        tot += folder_sizes[k]
print(tot)