import itertools

rules = {}
messages = None
for l in open('2020/19/input.txt'):
    l = l.strip()
    if not l:
        messages = []
        continue
    if messages is not None:
        messages.append(l)
    else:
        k, v = l.split(':')
        rules[k] = v.strip()

def values(i):
    r = rules[i]
    if r[0] == '"':
        return [r[1]]
    result = set()
    for alt in r.split('|'):
        subs = [values(t) for t in alt.split()]
        result |= set(''.join(l) for l in itertools.product(*subs))
    return result

good = values('0')
accepted = [l for l in messages if l in good]
print('one', len(accepted))

# 0: 8 11
# 8: 42 | 42 8
# 11: 42 31 | 42 11 31
# =>
# 1. 1..n times 42
# 2. 1..m times 42 followed by the same number of 31
values42 = set(values('42'))
values31 = set(values('31'))
assert all(len(t) == 8 for t in values42)
assert all(len(t) == 8 for t in values31)
assert values42.isdisjoint(values31)

def blocks(iterable, n):
    iterator = iter(iterable)
    while batch := tuple(itertools.islice(iterator, n)):
        yield ''.join(batch)

def testtwo(msg):
    if len(msg) % 8 != 0:
        return False
    fourtytwos = 0
    thirtyones = None
    for block in blocks(msg, 8):
        if thirtyones is None:
            if block in values42:
                fourtytwos += 1
            else:
                thirtyones = 0
        if thirtyones is not None:
            if block in values31:
                thirtyones += 1
            else:
                return False
    if thirtyones is None:
        return False
    if thirtyones == 0 or fourtytwos == 0:
        return False
    return fourtytwos-thirtyones >= 1

two = 0
for msg in messages:
    if testtwo(msg):
        two += 1
print('two', two)
