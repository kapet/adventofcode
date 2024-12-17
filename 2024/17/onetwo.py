with open('2024/17/input.txt') as f:
    regs = [int(f.readline().split()[2]) for _ in range(3)]
    f.readline()
    prog = list(map(int, f.readline().split()[1].split(',')))

def run(regs):
    ip = 0
    output = []
    while ip < len(prog):
        opcode, operand = prog[ip:ip+2]
        ip += 2

        match operand:
            case 0 | 1 | 2 | 3: # literal
                combo = operand
            case 4 | 5 | 6: # register value
                combo = regs[operand-4]
            case 7: # illegal
                combo = None

        match opcode:
            case 0: # adv
                regs[0] = regs[0] // (2**combo)
            case 1: # bxl
                regs[1] = regs[1] ^ operand
            case 2: # bst
                regs[1] = combo & 7
            case 3: # jnz
                if regs[0]:
                    ip = operand
            case 4: # bxc
                regs[1] = regs[1] ^ regs[2]
            case 5: # out
                yield combo & 7
            case 6: # bdv
                regs[1] = regs[0] // (2**combo)
            case 7: # cdv
                regs[2] = regs[0] // (2**combo)
    return output

def run2(regs):
    a, b, c = regs
    output = []
    while True:
        b = a & 7
        b = b ^ 3
        c = a // (2**b)  # shift right by B bits
        b = b ^ c
        a = a // (2**3)  # shift right by 3 bits
        b = b ^ 5
        output.append(b & 7)
        if a == 0:
            return output

one = run2(regs[:])
print('one', ','.join(str(o) for o in one))

_ = '''
always takes 3 bits from a for every output
last number outputted is highest bits
higher bits impact lower bits, but not vice versa
-> start looking for last output first

0 -> 0o6
3, 0 -> 0o61, 0o65
5, 3, 0 -> 0o611, 0o615, 0o651, 0o655, 0o656
5, 5, 3, 0 -> 0o6111, 0o6117, 0o6151, 0o6511, 0o6517, 0o6551, 0o6562
'''

base = [0] # start with no bits set at all
for i in range(len(prog)):
    goal = prog[-1-i:]
    newbase = []
    for b in base:
        # which extra bits give us the right result?
        for j in range(8):
            t = b * 8 + j
            if goal == run2([t, 0, 0]):
                newbase.append(t)
    base = newbase
print('two', min(base))
