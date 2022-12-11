from math import prod

class Monkey:
    def __init__(self, _starting_items, _operation, _test, _true, _false) -> None:
        self.items = _starting_items
        self.operation = _operation
        self.test = _test
        self.true = _true
        self.false = _false
        self.counted = 0
    
    def count(self):
        self.counted += 1

    def __repr__(self) -> str:
        return str(self.counted)

with open('input.txt') as f:
    instructions = ''.join([x for x in f])

monkeys = []
for instruction in instructions.split('\n\n'):
    data = instruction.split('\n')
    starting_items = [int(x) for x in data[1][18:].replace(',', '').split()]
    operation = [x for x in data[2][13:].split()]
    test = int(data[3][21:])#divisible by
    if_true = int(data[4][29:]) #throw to monkey
    if_false = int(data[5][30:]) #throw to monkey
    monkeys.append(Monkey(starting_items, operation, test, if_true, if_false))

mod_op = prod(monkey.test for monkey in monkeys)

for i in range(10000):
    for monkey in monkeys:
        while len(monkey.items) > 0:
            first = monkey.operation[2]
            op = monkey.operation[3]
            second = monkey.operation[4]
            item = monkey.items.pop(0)
            
            if first == 'old':
                first = item
            if second == 'old':
                second = item
            if op == '+':
                worry = int(first) + int(second)
            else:
                worry = (int(first) * int(second))
            worry %= mod_op
            if worry % monkey.test == 0:
                monkeys[monkey.true].items.append(worry)
            else:
                monkeys[monkey.false].items.append(worry)
            monkey.counted += 1

s = []
for monkey in monkeys:
        s.append(monkey.counted)
s.sort(reverse=True)
print(s[0] * s[1])
