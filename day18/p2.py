from collections import deque
with open('input.txt') as f:
    coordinates = [x.strip() for x in f]

points = set()

for coordinate in coordinates:
    x, y, z = coordinate.split(',')
    points.add((int(x),int(y),int(z)))

def adjecent(x, y, z):
    return [(x+1, y, z), (x-1, y, z), (x, y+1, z), (x, y-1, z), (x, y, z+1), (x, y, z-1)]

res = 0
min_pt = tuple(min(a[i] - 1 for a in points) for i in range(3))
max_pt = tuple(max(a[i] + 1 for a in points) for i in range(3))

seen = set()
queue = deque([min_pt])
while queue:
    cur = queue.popleft()
    if cur in seen:
        continue
    seen.add(cur)
    for adj_pt in adjecent(*cur):
        if adj_pt in points:
            res += 1
        elif adj_pt not in queue and all(min_pt[i] <= adj_pt[i] <= max_pt[i] for i in range(3)):
            queue.append(adj_pt)

print(res)