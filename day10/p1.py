with open('input.txt') as f:
    lines = [x.rstrip() for x in f]


def check_cycle():
    global cycles
    global sig_strength

    if cycles == 20 or cycles % 40 == 20:
        sig_strength += cycles*reg_x

reg_x = 1
cycles = 0
sig_strength = 0
for line in lines:
    line = line.split()
    if line[0] == 'noop':
        cycles += 1
        check_cycle()
    elif line[0] == 'addx':
        for _ in range(2):
            cycles += 1
            check_cycle()
        reg_x += int(line[1])
print(sig_strength)