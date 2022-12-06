line = open('input.txt').readline().rstrip()

idx = 0
for i in range(len(line)):
    d = set()

    [d.add(line[x]) for x in range(idx, idx+4)]

    if(len(d) == 4):
        print(i + 4)
        exit()
    idx += 1