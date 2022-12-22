import pprint
import re
with open('input.txt') as f:
    lines = [x.rstrip() for x in f]

class monkey:
    def __init__(self, name, value) -> None:
        self.name = name
        self.value = value

    def __hash__(self) -> int:
        return hash(self.name)

d = {}

for line in lines:
    n = line[:4]
    val = line[6:]
    d[n] = val

notsolved = True
while notsolved:
    for i in d.items():
        if i[0] == 'root':
            if isinstance(i[1], int):
                print(i)
                exit()
        if not isinstance(i[1], int):
            val = i[1].split()
            if len(val) > 1:
                if not isinstance(val[0], int) and not val[0].isnumeric():
                    numeric = False
                    try:
                        numeric = d[val[0]].isnumeric()
                    except:
                        numeric = isinstance(d[val[0]], int)
                    if numeric:
                        val[0] = d[val[0]]
                        d[i[0]] = ' '.join([str(x) for x in val])
                if not isinstance(val[2], int) and not val[2].isnumeric():
                    numeric = False
                    try:
                        numeric = d[val[2]].isnumeric()
                    except:
                        numeric = isinstance(d[val[2]], int)
                    if numeric:
                        val[2] = d[val[2]]
                        d[i[0]] = ' '.join([str(x) for x in val])
                
                
                x = d[i[0]].split()
                if x[0].isnumeric() and x[2].isnumeric():
                    try:
                        match x[1]:
                            case '+':
                                d[i[0]] = int(x[0]) + int(x[2])
                            case '-':
                                d[i[0]] = int(x[0]) - int(x[2])
                            case '/':
                                d[i[0]] = int(x[0]) // int(x[2])
                            case '*':
                                d[i[0]] = int(x[0]) * int(x[2])
                    except:
                        print(i)