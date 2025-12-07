import itertools
import math

rawdata = open("2025/06/input.txt").readlines()

data = [l.strip().split() for l in rawdata]
rows = len(data)-1
number_of_problems = len(data[0])
ops = data[-1]
one = 0
for x in range(number_of_problems):
    result = int(data[0][x])
    op = ops[x]
    assert op in "*+"
    for y in range(1, rows):
        n = int(data[y][x])
        if op == '+':
            result += n
        else:
            result *= n
    one += result
print("one", one)

# transpose the table so columns combine into rows
data = list(map(lambda x: ''.join(x).strip(), zip(*rawdata[:-1])))
# separate problems into sub-lists
data = [list(l) for space, l in itertools.groupby(data, lambda x: x == '') if not space]
# parse numbers
data = [[int(i) for i in l] for l in data]
two = 0
for x in range(number_of_problems):
    numbers = data[x]
    op = ops[x]
    if op == '+':
        two += math.fsum(numbers)
    else:
        two += math.prod(numbers)
print("two", int(two))





