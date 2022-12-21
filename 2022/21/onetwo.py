monkeys_known = {}
monkeys_unknown = []

for line in open('2022/21/input.txt'):
    line = line.split()
    line[0] = line[0][:-1] # drop : from name
    if len(line) == 2:
        monkeys_known[line[0]] = int(line[1])
        print('  ', line[0], '=', line[1])
    elif len(line) == 4:
        monkeys_unknown.append(line)
    else:
        raise Exception()

i = 0
while 'root' not in monkeys_known:
    name, m1, op, m2 = monkeys_unknown[i]

    if m1 in monkeys_known and m2 in monkeys_known:
        monkeys_unknown.pop(i)
        if op == '+':
            value = monkeys_known[m1] + monkeys_known[m2]
        elif op == '-':
            value = monkeys_known[m1] - monkeys_known[m2]
        elif op == '*':
            value = monkeys_known[m1] * monkeys_known[m2]
        elif op == '/':
            value = monkeys_known[m1] // monkeys_known[m2]
        else:
            raise Exception()
        monkeys_known[name] = value
        print('  ', name, '=', value)
    else:
        i += 1

    if i >= len(monkeys_unknown):
        i = 0

print('one:', monkeys_known['root'])
