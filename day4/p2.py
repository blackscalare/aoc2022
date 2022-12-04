with open('input.txt') as f:
    lines = [x.rstrip() for x in f]

def any_overlap(p1, p2):
    p1_s, p1_e = p1.split('-')
    p2_s, p2_e = p2.split('-')
    r1 = range(int(p1_s), int(p1_e) + 1)
    r2 = range(int(p2_s), int(p2_e) + 1)

    if any(x in r1 for x in r2):
        return 1
    if any(x in r2 for x in r1):
        return 1
    return 0

tot = 0
for line in lines:
    p1, p2 = line.split(',')
    tot += any_overlap(p1, p2)

print(tot)