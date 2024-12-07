import functools
import math

equations = []
for l in open('2024/07/input.txt'):
    result, operands = l.split(':')
    operands = map(int, operands.split())
    equations.append((int(result), list(operands)))

@functools.cache
def concat(a, b):
    return int(str(a) + str(b))

@functools.cache
def calc(limit, os):
    if len(os) == 1:
        return os, os

    rest, o = os[:-1], os[-1]
    rest1, rest2 = calc(limit, rest)

    result1 = set()
    for v in rest1:
        for t in (v+o, v*o):
            if t <= limit:
                result1.add(t)

    result2 = set()
    for v in rest2:
        for t in (v+o, v*o, concat(v, o)):
            if t <= limit:
                result2.add(t)

    return result1, result2

one = two = 0
for r, os in equations:
    v1, v2 = calc(r, tuple(os))
    if r in v1:
        one += r
    if r in v2:
        two += r
print('one', one)
print('two', two)

assert one == 5837374519342
assert two == 492383931650959
