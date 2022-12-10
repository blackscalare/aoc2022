with open('input.txt') as f:
    lines = [x.rstrip() for x in f]

def draw(reg_x, cycles, screen):
    row = cycles // 40
    col = cycles % 40
    
    sprite = [reg_x - 1, reg_x, reg_x + 1]

    if col in sprite:
        screen[row][col] = '█'
    else:
        screen[row][col] = '.'
    return screen

reg_x = 1
cycles = -1
screen = []
for _ in range(6):
    screen.append(['.' for _ in range(40)])

for line in lines:
    line = line.split()
    if line[0] == 'noop':
        cycles += 1
        draw(reg_x, cycles, screen)
    elif line[0] == 'addx':
        for _ in range(2):
            cycles += 1
            draw(reg_x, cycles, screen)
        reg_x += int(line[1])

for row in screen:
    print(''.join(row))
