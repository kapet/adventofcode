instructions = []
for l in open('2020/08/input.txt'):
    op, val = l.split()
    val = int(val)
    instructions.append((op, val))

def execute(instruct):
    acc = 0
    pc = 0
    done = set()
    while pc != len(instruct):
        if pc in done:
            return False, acc
        if pc > len(instruct):
            return False, None
        done.add(pc)
        op, val = instruct[pc]
        if op == 'acc':
            acc += val
            pc += 1
        elif op == 'jmp':
            pc += val
        elif op == 'nop':
            pc += 1
        else:
            raise Exception()
    return True, acc

print('one', execute(instructions)[1])

for c in range(len(instructions)):
    instruct = instructions[:]
    if instructions[c][0] == 'nop':
        instruct[c] = ('jmp', instruct[c][1])
    elif instructions[c][0] == 'jmp':
        instruct[c] = ('nop', instruct[c][1])
    else:
        continue
    ok, two = execute(instruct)
    if ok:
        break
print('two', two)
