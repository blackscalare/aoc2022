with open('input.txt') as f:
    lines = [x.rstrip() for x in f]

def distance(a, b):
    return abs(a - b)

def calc_knots():
    for i in range(1, len(ropes)):
        dist_x = distance(ropes[i-1][0], ropes[i][0])
        dist_y = distance(ropes[i-1][1], ropes[i][1])
        if dist_x > 1:
            if dist_y <= 1:
                ropes[i][1] = ropes[i - 1][1]
            if ropes[i - 1][0] > ropes[i][0]:
                ropes[i][0] = ropes[i - 1][0] - 1
            else:
                ropes[i][0] = ropes[i - 1][0] + 1
        
        if dist_y > 1:
            if dist_x <= 1:
                ropes[i][0] = ropes[i - 1][0]
            if ropes[i - 1][1] > ropes[i][1]:
                ropes[i][1] = ropes[i - 1][1] - 1
            else:
                ropes[i][1] = ropes[i - 1][1] + 1
        t_visited.add((ropes[-1][0], ropes[-1][1]))
        

ropes = [[0,0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
t = [0, 0]

t_visited = set()

t_visited.add((0,0))
for line in lines:
    direction, steps = line.split()
    match direction:
        case 'U':
            for _ in range(1, int(steps) + 1):
                ropes[0][1] -= 1
                calc_knots()
        case 'R':
            for _ in range(int(steps)):
                ropes[0][0] += 1
                calc_knots()
        case 'D':
            for _ in range(int(steps)):
                ropes[0][1] += 1
                calc_knots()
        case 'L':
            for _ in range(int(steps)):
                ropes[0][0] -= 1
                calc_knots()
    
print(len(t_visited))