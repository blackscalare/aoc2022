with open('input.txt') as f:
    lines = [x.rstrip().split(' -> ') for x in f]

points = set()

for line in lines:
    for i in range(len(line) - 1):
        x1, y1 = line[i].split(',')
        x2, y2 = line[i + 1].split(',')

        x1, x2 = sorted([int(x1), int(x2)])
        y1, y2 = sorted([int(y1), int(y2)])

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                points.add((x,y))

floor = max(y for x, y in points)
highest = 0
for i in range(-1000, 1000):
    points.add((i, floor + 2))

not_freefall = True
count = 0
while not_freefall:
    s = [500, 0]
    if (500,0) in points:
        break
    while True:
        
        if (s[0], s[1] + 1) not in points:
            s[1] += 1
        elif (s[0], s[1] + 1) in points:
            if (s[0] - 1, s[1] + 1) not in points:
                s[0] -= 1
                s[1] += 1
            elif (s[0] + 1, s[1] + 1) not in points:
                s[0] += 1
                s[1] += 1
            else:
                points.add((s[0], s[1]))
                count += 1
                break
print(count)


