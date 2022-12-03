with open('input.txt') as f:
    lines = [x.rstrip() for x in f]

tot = 0

def get_value(c):
    if c.islower():
        return ord(c) - 96
    else:
        return ord(c) - 38

for line in lines:
    comp1 = line[:int(len(line) / 2)]
    comp2 = line[int(len(line) / 2):]
    for c in comp1:
        if c in comp2:
            tot += get_value(c)
            break
print(tot)