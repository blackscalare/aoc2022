line = open('input.txt').readline().rstrip()

idx = 0
for i in range(len(line)):
    d = set()

    [d.add(line[x]) for x in range(idx, idx+14)]

    if(len(d) == 14):
        print(i + 14)
        exit()
    idx += 1