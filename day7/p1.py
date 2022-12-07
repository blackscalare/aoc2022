from collections import defaultdict
from anytree import Node
with open('test.txt') as f:
    lines = [x.rstrip() for x in f]

EXEC = '$'
CD = 'cd'
LS = 'ls'
ls_mode = False
nodes = {}
current_dir = ''
last_dir = ''
current_node = None
last_node = ''
for line in lines:
    line = line.split(' ')
    op = line[0]

    if op == EXEC or op == CD:
        ls_mode = False
    
    if ls_mode:
        if line[0].isnumeric():
            nodes[current_dir][current_node] += int(line[0])
        else:
            pass

    if op == EXEC:
        if line[1] == CD:
            last_dir = current_dir
            last_node = current_node
            d = line[2]
            if d == '..':
                nodes[last_dir]
            elif d == '/':
                current_dir = d
                if d not in nodes.keys():
                    nodes[d] = {Node(d): 0}
                current_node = list(nodes[d])[0]
            else:
                if d not in nodes.keys():
                    nodes[d] = {Node(d, parent=list(nodes[last_dir])[0]): 0}
                    current_dir = d
                    current_node = list(nodes[d])[0]
                else:
                    children = [x for x in list(nodes[d])[0].children]
        elif line[1] == LS:
            ls_mode = True
for l in nodes.keys():
    print(list(nodes[l].keys())[0].ancestors)