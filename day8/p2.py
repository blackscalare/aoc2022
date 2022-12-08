class Tree():
    def __init__(self, h, coord, score = 0):
        self.h = h
        self.coord = coord
        self.score = score

with open('input.txt') as f:
    lines = [x.rstrip() for x in f]

trees = {}

for y, line in enumerate(lines):
    for x, t in enumerate(line):
        trees[(x,y)] = Tree(int(t), (x,y))

def score_up(tree):
    score = 0
    orig_x = tree.coord[0]
    orig_y = tree.coord[1]
    curr_y = orig_y - 1
    while curr_y >= 0:
        score += 1
        h = trees[orig_x, curr_y].h
        if h >= tree.h:
            return score
        curr_y -= 1
    return score

def score_right(tree):
    score = 0
    orig_x = tree.coord[0]
    orig_y = tree.coord[1]
    curr_x = orig_x + 1
    while curr_x <= len(lines[0]) - 1:
        score += 1
        h = trees[curr_x, orig_y].h
        if h >= tree.h:
            return score
        curr_x += 1
    return score

def score_down(tree):
    score = 0
    orig_x = tree.coord[0]
    orig_y = tree.coord[1]
    curr_y = orig_y + 1
    while curr_y <= len(lines) - 1:
        score += 1
        h = trees[orig_x, curr_y].h
        if h >= tree.h:
            return score
        curr_y += 1
    return score

def score_left(tree):
    score = 0
    orig_x = tree.coord[0]
    orig_y = tree.coord[1]
    curr_x = orig_x - 1
    while curr_x >= 0:
        score += 1
        h = trees[curr_x, orig_y].h
        if h >= tree.h:
            return score
        curr_x -= 1
    return score

def get_score(tree):
    return score_up(tree) * score_right(tree) * score_down(tree) * score_left(tree)

for y in range(1, len(lines) - 1):
    for x in range(1, len(lines[0]) - 1):
        tree = trees[(x,y)]
        tree.score = get_score(tree)

t = 0
scores = []
for k in trees:
    tree = trees[k]
    scores.append(tree.score)

scores.sort(reverse=True)
print(scores[0])