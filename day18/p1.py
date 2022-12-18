with open('input.txt') as f:
    coordinates = [x.strip() for x in f]

points = set()

for coordinate in coordinates:
    x, y, z = coordinate.split(',')
    points.add((int(x),int(y),int(z)))

def adjecent(x, y, z):
    return [(x+1, y, z), (x-1, y, z), (x, y+1, z), (x, y-1, z), (x, y, z+1), (x, y, z-1)]
    
tot = 0
for point in points:
    sides = 6
    for adj_pt in adjecent(*point):
        if adj_pt in points:
            sides -= 1
    tot += sides
print(tot)