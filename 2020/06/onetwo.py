import collections

lines = open('2020/06/input.txt').read()
groups = [g.split('\n') for g in lines.split('\n\n')]

one = 0
two = 0
for g in groups:
    q = collections.Counter()
    for p in g:
        q.update(list(p))
    one += len(q)
    two += sum(1 for t in q.values() if t == len(g))
print('one', one)
print('two', two)
