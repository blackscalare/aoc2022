#!/bin/python3
with open('input.txt') as f:
    lines = [x.rstrip()for x in f]

fs = {'size': 0}
cwd = []

def populate(lines):
    for line in lines:
        line = line.split()
        if line[0] == '$':
            if line[1] == 'cd':
                if line[2] == '..':
                    cwd.pop()
                else:
                    cwd.append(line[2])
        else:
            current = fs
            for dir in cwd:
                current = current[dir]
            if line[0] == 'dir':
                if line[1] not in current.keys():
                    current[line[1]] = {}
            else:
                value = int(line[0])
                fs['size'] += value
                current = fs
                for dir in cwd:
                    current = current[dir]
                    if 'size' in current:
                        current['size'] += value
                    else:
                        current['size'] = value

def get_sizes(fs, sizes):
    for key in fs.keys():
        if type(fs[key]) is dict:
            get_sizes(fs[key], sizes)
    sizes.append(fs['size'])

populate(lines[1:])

sizes = []
get_sizes(fs, sizes)
s = sum([int(x) for x in sizes if int(x) <= 100000])
print(s)