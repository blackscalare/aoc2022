with open('input.txt') as f:
    lines = [x.rstrip() for x in f]

def get_value(c):
    if c.islower():
        return ord(c) - 96
    else:
        return ord(c) - 38

def check(g):
    for c in g[0]:
        if c in g[1]:
            return get_value(c)

print(sum([check([x[:len(x) // 2], x[len(x) // 2:]]) for x in lines]))