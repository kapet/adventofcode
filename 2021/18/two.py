from snailfish import *

def max_magnitude(filename):
    values = []
    for line in open(filename):
        line = line.strip()  # remove trailing \n
        values.append(parse(line))

    max_ = 0
    for x in range(len(values)):
        for y in range(len(values)):
            if x == y:
                # don't add number to itself
                continue
            val = add(values[x], values[y])
            reduce(val)
            m = magnitude(val)
            if m > max_:
                max_ = m
    return max_

# example homework
assert max_magnitude('2021/18/test.txt') == 3993

# actual exercise
print(max_magnitude('2021/18/input.txt'))
