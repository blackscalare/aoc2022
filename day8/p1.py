class Tree():
    def __init__(self, h, coord, visible = False):
        self.h = h
        self.coord = coord
        self.visible = visible

with open('input.txt') as f:
    lines = [x.rstrip() for x in f]

trees = {}

edge_x = (0, len(lines) - 1)
edge_y = (0, len(lines) - 1)
for y, line in enumerate(lines):
    for x, t in enumerate(line):
        if x in edge_x or y in edge_y:
            trees[(x, y)] = Tree(int(t), (x,y), visible=True)
        else:
            trees[(x,y)] = Tree(int(t), (x,y))

def vis_up(tree):
    orig_x = tree.coord[0]
    orig_y = tree.coord[1]
    curr_y = orig_y - 1
    while curr_y >= 0:
        h = trees[orig_x, curr_y].h
        if h >= tree.h:
            return False
        curr_y -= 1
    return True

def vis_right(tree):
    orig_x = tree.coord[0]
    orig_y = tree.coord[1]
    curr_x = orig_x + 1
    while curr_x <= len(lines[0]) - 1:
        h = trees[curr_x, orig_y].h
        if h >= tree.h:
            return False
        curr_x += 1
    return True

def vis_down(tree):
    orig_x = tree.coord[0]
    orig_y = tree.coord[1]
    curr_y = orig_y + 1
    while curr_y <= len(lines) - 1:
        h = trees[orig_x, curr_y].h
        if h >= tree.h:
            return False
        curr_y += 1
    return True

def vis_left(tree):
    orig_x = tree.coord[0]
    orig_y = tree.coord[1]
    curr_x = orig_x - 1
    while curr_x >= 0:
        h = trees[curr_x, orig_y].h
        if h >= tree.h:
            return False
        curr_x -= 1
    return True

def check_visibility(tree):
    return vis_up(tree) or vis_right(tree) or vis_down(tree) or vis_left(tree)

for y in range(1, len(lines) - 1):
    for x in range(1, len(lines[0]) - 1):
        tree = trees[(x,y)]
        tree.visible = check_visibility(tree)

t = 0
for k in trees:
    tree = trees[k]
    if tree.visible:
        t += 1
print(t)