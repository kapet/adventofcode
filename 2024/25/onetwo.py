import itertools

# split data into blocks of keys and locks
data = open('2024/25/input.txt').read().split('\n\n')
# split each block into lines
data = [list(map(list, d.split('\n'))) for d in data]
# rotate each block so that code is in rows not in columns
data = [list(zip(*d)) for d in data]
# decode and sort blocks
locks = set()
keys = set()
for d in data:
    value = tuple(t.count('#')-1 for t in d)
    if d[0][0] == '.':
        keys.add(value)
    else:
        locks.add(value)

one = 0
for key, lock in itertools.product(keys, locks):
    if all(key[i]+lock[i] <= 5 for i in range(5)):
        one += 1
print('one', one)
