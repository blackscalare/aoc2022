line = open('input.txt').readline().rstrip()

for i in range(len(line)):
    if len(set(line[i:i+4])) == 4:
        print(i + 4)
        exit()