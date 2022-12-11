class Monkey:
    def __init__(self, items, op, testDivisor, targets):
        self.items = items
        self.op = op
        self.testDivisor = testDivisor
        self.targets = targets

monkeys = []

if 0:
    # Test
    monkeys.append(Monkey([79, 98],         lambda x: x*19, 23, (2, 3)))
    monkeys.append(Monkey([54, 65, 75, 74], lambda x: x+6,  19, (2, 0)))
    monkeys.append(Monkey([79, 60, 97],     lambda x: x*x,  13, (1, 3)))
    monkeys.append(Monkey([74],             lambda x: x+3,  17, (0, 1)))
else:
    # Input
    monkeys.append(Monkey([84, 66, 62, 69, 88, 91, 91],     lambda x: x*11,  2, (4, 7)))
    monkeys.append(Monkey([98, 50, 76, 99],                 lambda x: x*x,   7, (3, 6)))
    monkeys.append(Monkey([72, 56, 94],                     lambda x: x+1,  13, (4, 0)))
    monkeys.append(Monkey([55, 88, 90, 77, 60, 67],         lambda x: x+2,   3, (6, 5)))
    monkeys.append(Monkey([69, 72, 63, 60, 72, 52, 63, 78], lambda x: x*13, 19, (1, 7)))
    monkeys.append(Monkey([89, 73],                         lambda x: x+5,  17, (2, 0)))
    monkeys.append(Monkey([78, 68, 98, 88, 66],             lambda x: x+6,  11, (2, 5)))
    monkeys.append(Monkey([70],                             lambda x: x+7,   5, (1, 3)))

if 0: # ONE
    inspected = [0]*len(monkeys)
    for round in range(20):
        for turn in range(len(monkeys)):
            monkey = monkeys[turn]
            while monkey.items:
                inspected[turn] += 1
                item = monkey.items.pop(0)
                # inspect
                worry = monkey.op(item)
                # relief
                worry = worry // 3
                # test & throw
                if worry % monkey.testDivisor == 0:
                    target = monkey.targets[0]
                else:
                    target = monkey.targets[1]
                monkeys[target].items.append(worry)

    inspected.sort()
    print('one:', inspected[-2]*inspected[-1])

else: # TWO
    # combine all individual divisors into a big one, operate in a 'ring'
    ringMod = 1
    for monkey in monkeys:
        ringMod *= monkey.testDivisor
    inspected = [0]*len(monkeys)
    for round in range(1, 10000+1):
        for turn in range(len(monkeys)):
            monkey = monkeys[turn]
            while monkey.items:
                inspected[turn] += 1
                item = monkey.items.pop(0)
                # inspect
                worry = monkey.op(item)
                # relief
                if worry >= ringMod:
                    worry = worry % ringMod
                # test & throw
                if worry % monkey.testDivisor == 0:
                    target = monkey.targets[0]
                else:
                    target = monkey.targets[1]
                monkeys[target].items.append(worry)

        if round in (1, 20, 1000, 5000, 10000):
            print(inspected)

    inspected.sort()
    print('one:', inspected[-2]*inspected[-1])
