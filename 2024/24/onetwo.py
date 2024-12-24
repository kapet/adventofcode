import collections

with open('2024/24/input.txt') as f:
    vars = {}
    while l := f.readline().strip():
        name, value = l.split(':')
        vars[name] = bool(int(value))

    ops = []
    while l := f.readline():
        v1, op, v2, _, v3 = l.split()
        ops.append([v1, op, v2, v3])

def i2v(x, y):
    vars = collections.defaultdict(bool)
    for i, c in enumerate(reversed(bin(x)[2:])):
        vars[f'x{i:02}'] = c == '1' and True or False
    for i, c in enumerate(reversed(bin(y)[2:])):
        vars[f'y{i:02}'] = c == '1' and True or False
    return vars

def v2i(vars):
    out = sorted((v for v in vars.keys() if v.startswith('z')), reverse=True)
    if out:
        return int(''.join(vars[v] and '1' or '0' for v in out), base=2)
    else:
        return 0

def solve(vars):
    keepgoing = True
    while keepgoing:
        keepgoing = False
        for v1, op, v2, v3 in ops:
            if (((v1[0] in 'xy') or (v1 in vars)) and
                ((v2[0] in 'xy') or (v2 in vars)) and
                v3 not in vars):
                keepgoing = True
                if op == 'AND':
                    vars[v3] = vars[v1] and vars[v2]
                elif op == 'OR':
                    vars[v3] = vars[v1] or vars[v2]
                elif op == 'XOR':
                    vars[v3] = vars[v1] ^ vars[v2]
                else:
                    raise Exception()

solve(vars)
print('one', v2i(vars))

# two, 1st step: output graph
with open('2024/24/out.dot', 'w') as f:
    f.write('digraph G {\n')
    for i, (v1, op, v2, v3) in enumerate(ops):
        f.write(f'{{{v1} {v2}}} -> {op}{i} -> {v3};\n')
    f.write('}\n')

# conclusion: highly localized, easy to spot wrong connections

# two, 3rd step: use info from 2nd step below and visually identify broken nodes
fixes = [
    (51, 'hmk'), (215, 'z16'),
    (185, 'fhp'), (44, 'z20'),
    (99, 'rvf'), (217, 'tpc'),
    (107, 'z33'), (161, 'fcd'),
]
for i,f in fixes:
    ops[i][3] = f

# two, 2nd step: try all individual bits, show where it goes wrong
for x in range(45):
    y = 1<<x
    twovars = i2v(y, y)
    solve(twovars)
    if v2i(twovars) != y+y:
        print('FAIL:', x, y, v2i(twovars))

# two, show final result
print('two', ','.join(sorted(f for _,f in fixes)))
