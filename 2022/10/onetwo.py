cycle = 0
register = 1

# ONE
sum_strength = 0

# TWO
crt = []

for line in open('input.txt'):
    cmd = line.split()
    # if cmd is 'noop' then just do a single step
    steps = [0]
    if cmd[0] == 'addx':
        # for 'addx' do a noop and then add the given constant
        steps = [0, int(cmd[1])]
    for step in steps:
        cycle += 1

        # ONE
        if (cycle-20)%40 == 0 and cycle <= 220:
            strength = cycle * register
            sum_strength += strength

        # TWO
        posInLine = (cycle-1) % 40
        if posInLine == 0:
            crt.append([])
        if abs(posInLine - register) <= 1:
            crt[-1].append('#')
        else:
            crt[-1].append('.')

        # an 'addx' command is executed at the _end_ of a step
        register += step

print('one:', sum_strength)

print('two:')
for row in crt:
    print(''.join(row))
