import functools

with open('2024/19/input.txt') as f:
    available = [l.strip() for l in f.readline().split(',')]
    f.readline()
    desired = [l.strip() for l in f]

avail = {}
for a in available:
    avail.setdefault(a[0], []).append(a)

@functools.cache
def combinations(pattern):
    result = 0
    for a in avail.get(pattern[0], []):
        if pattern[:len(a)] == a:
            if len(a) == len(pattern):
                result += 1
            else:
                result += combinations(pattern[len(a):])
    return result

one = 0
two = 0
for d in desired:
    c = combinations(d)
    if c:
        one += 1
    two += c

print('one', one)
print('two', two)
