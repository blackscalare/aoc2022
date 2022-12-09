with open('input.txt') as f:
    lines = [x.rstrip() for x in f]

def distance(a, b):
    return abs(a - b)

h = [0, 0]
t = [0, 0]

t_visited = set()

t_visited.add((0,0))
for line in lines:
    direction, steps = line.split()
    match direction:
        case 'U':
            for _ in range(1, int(steps) + 1):
                h[1] -= 1
                if distance(h[1], t[1]) <= 1 and distance(h[0], t[0]) <= 1:
                    continue
                else:
                    t[0] = h[0]
                    t[1] = h[1] + 1
                    t_visited.add((t[0], t[1]))
        case 'R':
            for _ in range(int(steps)):
                h[0] += 1
                if distance(h[1], t[1]) <= 1 and distance(h[0], t[0]) <= 1:
                    continue
                else:
                    t[0] = h[0] - 1
                    t[1] = h[1]
                    t_visited.add((t[0], t[1]))
        case 'D':
            for _ in range(int(steps)):
                h[1] += 1
                if distance(h[1], t[1]) <= 1 and distance(h[0], t[0]) <= 1:
                    continue
                else:
                    t[0] = h[0]
                    t[1] = h[1] - 1 
                    t_visited.add((t[0], t[1]))
        case 'L':
            for _ in range(int(steps)):
                h[0] -= 1
                if distance(h[1], t[1]) <= 1 and distance(h[0], t[0]) <= 1:
                    continue
                else:
                    t[0] = h[0] + 1
                    t[1] = h[1]
                    t_visited.add((t[0], t[1]))
print(len(t_visited))