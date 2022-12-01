with open('input.txt') as f:
    lines = f.readlines()

elves = []

elf_tot = 0
for line in lines:
    if(line == '\n'):
        elves.append(elf_tot)
        elf_tot = 0
        continue
    else:
        elf_tot += int(line)

elves.sort(reverse=True)

print(elves[0] + elves[1] + elves[2])