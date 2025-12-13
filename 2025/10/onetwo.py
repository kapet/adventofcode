data = []
for l in open("2025/10/input.txt"):
    indicators, l = l.split(']')
    switches, joltages = l.split('{')
    # "#.." -> "100"
    indicators = indicators[1:].translate({ord("."): "0", ord("#"): "1"})
    # "(0,1)" -> [0,1]
    switches = [
        [int(i) for i in s[1:-1].split(",")]
        for s in switches.strip().split()
    ]
    # [0,1] -> "110"
    switches = [
        ''.join((i in s) and "1" or "0" for i in range(len(indicators)))
        for s in switches
    ]
    joltages = [int(j) for j in joltages.strip()[:-1].split(',')]
    assert len(indicators) == len(switches[0]) == len(joltages)
    data.append((indicators, switches, joltages))

if 0:
    i1 = int(indicators[1:].replace(".", "0").replace("#", "1")[::-1], 2)
    for s in switches:
        r = 0
        for i in s[1:-1].split(','):
            r |= 1 << int(i)
        switches.append(r)

# idea: which combination of switches xor'ed together give the indicators?
# - same as: which switches xor'ed with the expected indicators give 0?
# - no ordering!
# - same button cancels itself -> every button may only be included once

def _find_one(indicators, switches):
    # this automatically gives a min-heap because presses naively increment
    stack = [(0, indicators, switches)]  # 0 presses, expected indicators, all switches
    done = set()  # nothing analyzed yet
    while stack:
        e = stack.pop(0)
        if e in done:
            # done this combination of #pressed/indicators/switches already!
            # this can happen because e.g. a->b->c->d is same as a->c->b->d
            continue
        done.add(e)
        presses, indicators, switches = e
        for si, s in enumerate(switches):
            # try pressing every remaining switch in turn
            i = indicators ^ s
            if i == 0:
                # found the solution!
                return presses + 1
            # not found yet, try the remaining switches later
            ns = switches[:si] + switches[si+1:]
            stack.append((presses+1, i, ns))
    raise Exception

one = 0
for indicators, switches, _ in data:
    # need everything as a number to xor it together
    indicators = int(indicators, 2)
    switches = tuple(int(i, 2) for i in switches)
    one += _find_one(indicators, switches)
print("one", one)

# idea: this is a linear system like: Ax=b 
# (A=button-indicator matrix, b=expected joltages vector, x=number of presses vector)
# e.g. for buttons (0,1) (1,1) and expected joltages (5,7) and presses (a,b)
#         (0,1)*(a,b)=(5,7) => (b, a+b)=(5,7) => b=5, a=2
#         (1,1)
# But we have often more or less buttons than indicators, so the matrix is not square.
# Math is hard, let's use https://github.com/coin-or/pulp

import pulp
two = 0
for _, switches, joltages in data:
    m = len(joltages)
    n = len(switches)

    # matrix with one row per joltage and one column per switch
    # 1=switch increments joltage, 0=it does not
    A = [[int(s[i]) for s in switches] for i in range(m)]

    # vector with one column per expected joltage
    b = joltages

    # vector with one column per switch
    x = [pulp.LpVariable(f"x_{s}", lowBound=0, cat="Integer") for s in range(n)]

    # goal is to minimize the sum of values in vector x
    p = pulp.LpProblem("two", pulp.LpMinimize)
    p += pulp.lpSum(x)

    # add all the Ax=b equations as constraints
    for j in range(m):
        p += pulp.lpSum(A[j][s]*x[s] for s in range(n)) == b[j]

    # now solve it
    p.solve(pulp.PULP_CBC_CMD(msg=False))
    assert p.status==1 # "Optimal"
    two += sum(v.value() for v in x)
print("two", two)
