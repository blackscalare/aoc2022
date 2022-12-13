from itertools import zip_longest
from functools import cmp_to_key

with open('input.txt') as f:
    pairs = f.read().split('\n\n')

def compare(l, r):
    if type(l) == int and not type(r) == int:
        l = [l]
    elif not type(l) == int and type(r) == int:
        r = [r]
    
    if type(l) == int and type(r) == int:
        if l < r:
            return -1
        elif l == r:
            return 0
        else:
            return 1
    else:
        for ll, rr in zip_longest(l, r):
            if ll is None:
                return -1
            elif rr is None:
                return 1
            res = compare(ll, rr)
            if res != 0:
                return res
        return 0

divider0 = [[2]]
divider1 = [[6]]
packets = []

for i, pair in enumerate(pairs):
    pair = pair.split()
    p1 = eval(pair[0])
    p2 = eval(pair[1])
    packets.extend([p1, p2])

packets.extend([divider0, divider1])

packets.sort(key=cmp_to_key(compare))

print((packets.index(divider0) + 1) * (packets.index(divider1) + 1))
