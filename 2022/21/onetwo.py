def calc(monkeys):
    monkeys_next = {}
    monkeys_known = {}
    while 'root' not in monkeys_known:
        for name, value in monkeys.items():
            if len(value) == 1:
                value = value[0]
                monkeys_known[name] = value
                #print('  ', name, '=', value)
                continue

            m1, op, m2 = value
            if m1 in monkeys_known and m2 in monkeys_known:
                if op == '+':
                    value = monkeys_known[m1] + monkeys_known[m2]
                elif op == '-':
                    value = monkeys_known[m1] - monkeys_known[m2]
                elif op == '*':
                    value = monkeys_known[m1] * monkeys_known[m2]
                elif op == '/':
                    d,m = divmod(monkeys_known[m1], monkeys_known[m2])
                    if m == 0:
                        # avoid float if we can
                        value = d
                    else:
                        value = monkeys_known[m1] / monkeys_known[m2]
                    value = monkeys_known[m1] / monkeys_known[m2]
                else:
                    raise Exception()
                monkeys_known[name] = value
                #print('  ', name, '=', value)
            else:
                monkeys_next[name] = value
        monkeys = monkeys_next

    return monkeys_known['root']


monkeys = {}
for line in open('2022/21/input.txt'):
    line = line.split()
    line[0] = line[0][:-1] # drop : from name
    if len(line) == 2:
        monkeys[line[0]] = (int(line[1]),)
    elif len(line) == 4:
        monkeys[line[0]] = tuple(line[1:])
    else:
        raise Exception()

result = calc(monkeys)
print('one:', result)

# we will look for same value on left and right side, will result in 0 if subtracted
monkeys['root'] = (monkeys['root'][0], '-', monkeys['root'][2])
def calc_human(monkeys, human):
    monkeys['humn'] = (human,)
    return calc(monkeys)

def sgn(value):
    return (value >= 0) and 1 or -1

# find interval left<right with zero crossing in between them
left = 0
left_result = calc_human(monkeys, left)
right = result
while True:
    right_result = calc_human(monkeys, right)
    if sgn(left_result) != sgn(right_result):
        break
    right *= 2

# bisect interval until zero crossing has been found
while True:
    midpoint = (left+right) // 2
    mid_result = calc_human(monkeys, midpoint)
    if mid_result == 0:
        break
    if sgn(left_result) == sgn(mid_result):
        left = midpoint
        left_result = mid_result
    else:
        right = midpoint
        right_result = mid_result

print('two:', midpoint)
