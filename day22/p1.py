import copy
import os
import time
with open('input.txt') as f:
    lines = [x.rstrip() for x in f]

world = {}
instructions = []
for y in range(len(lines)):
    tmp = ''
    if lines[y] == '':
        for x in range(len(lines[y + 1])):
            if lines[y+1][x].isalpha():
                tmp += ' '
                tmp += lines[y+1][x]
                tmp += ' '
            else:
                tmp += lines[y+1][x]
        instructions = tmp.split()
        break
    for x in range(len(lines[y])):
        if lines[y][x] != ' ':
            world[(y,x)] = lines[y][x]
minx = 9999999999999999999999
for w in world.keys():
    if w[0] == 0:
        if w[1] < minx:
            minx = w[1]

player = (0, minx)

R = (0, 1)
D = (1, 0)
L = (0, -1)
U = (-1, 0)

current_face = R


def find_min(world, curr, anchor, repl):
    _min = 9999999999999999999999
    for w in world.keys():
        if w[anchor] == curr:
            if w[repl] < _min:
              _min = w[repl]
    return _min

def find_max(world, curr, anchor, repl):
    _max = -9999999999999999999999
    for w in world.keys():
        if w[anchor] == curr:
            if w[repl] > _max:
                _max = w[repl]
    return _max
player_walk = {}
player_walk[player] = current_face
def print_map(world, player_walk):
    os.system('clear')
    for i in range(151):
        row = ''
        for j in range(201):
            #if (i,j) == player:
            if (i,j) in player_walk:
                match player_walk[(i,j)]:
                    case (0, 1): #R
                        row += '>'
                    case (1, 0): #D
                        row += 'v'
                    case (0, -1): #L
                        row += '<'
                    case (-1, 0): #U
                        row += '^'
            elif (i,j) in world:
                row += (world[(i,j)])
            else:
                row += ' '
        print(row)
    #time.sleep(0.1)
    input()

for instruction in instructions:
    #print_map(world, player_walk)

    if instruction.isnumeric():
        dist = int(instruction)
        for _ in range(dist):
            tmp_pos = (player[0] + current_face[0], player[1] + current_face[1])
            if tmp_pos in world:
                obj = world[tmp_pos]
                if obj == '.':
                    player = copy.deepcopy(tmp_pos)
                elif obj == '#':
                    break
            else:
                if current_face == R or current_face == L:
                    if current_face == R:
                        tmp_pos = (player[0], find_min(world, player[0], 0, 1))
                    else:
                        tmp_pos = (player[0], find_max(world, player[0], 0, 1))
                    if tmp_pos in world:
                        obj = world[tmp_pos]
                        if obj == '.':
                            player = copy.deepcopy(tmp_pos)
                        elif obj == '#':
                            break
                elif current_face == D or current_face == U:
                    if current_face == D:
                        tmp_pos = (find_min(world, player[1], 1, 0), player[1])
                    else:
                        tmp_pos = (find_max(world, player[1], 1, 0), player[1])
                    if tmp_pos in world:
                        obj = world[tmp_pos]
                        if obj == '.':
                            player = copy.deepcopy(tmp_pos)
                        elif obj == '#':
                            break
            player_walk[player] = current_face
    elif instruction.isalpha():
        if instruction == 'R':
            match current_face:
                case (0, 1): #R
                    current_face = D
                case (1, 0): #D
                    current_face = L
                case (0, -1): #L
                    current_face = U
                case (-1, 0): #U
                    current_face = R
        elif instruction == 'L':
            match current_face:
                case (0, 1): #R
                    current_face = U
                case (1, 0): #D
                    current_face = R
                case (0, -1): #L
                    current_face = D
                case (-1, 0): #U
                    current_face = L

print(player)
face_value = 0
match current_face:
    case (0, 1): #R
        face_value = 0
    case (1, 0): #D
        face_value = 1
    case (0, -1): #L
        face_value = 2
    case (-1, 0): #U
        face_value = 3
print(((player[0] + 1) * 1000) + ((player[1] + 1) * 4) + face_value)