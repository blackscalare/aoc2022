with open('input.txt') as f:
    lines = [x.rstrip() for x in f]

def get_value(c):
    if c.islower():
        return ord(c) - 96
    else:
        return ord(c) - 38

def check(g):
    for c in g[0]:
        if c in g[1] and c in g[2]:
            return get_value(c)
tot = 0
for i in range(0, len(lines), 3):
    g1 = lines[i]
    g2 = lines[i + 1]
    g3 = lines[i + 2]

    tot += check([g1, g2, g3])
print(tot)