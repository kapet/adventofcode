import itertools

data = [int(l) for l in open('2020/01/input.txt')]

for a, b in itertools.combinations(data, 2):
    if a+b == 2020:
        print('one', a*b)
        break

for a, b, c in itertools.combinations(data, 3):
    if a+b+c == 2020:
        print('two', a*b*c)
        break
