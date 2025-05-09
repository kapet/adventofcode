import collections

data = [l.strip().split(' = ') for l in open('2020/14/input.txt')]

memory = collections.defaultdict(int)
andmask = ormask = None
for cmd, value in data:
    if cmd == 'mask':
        andmask = int(value.replace('X', '1'), 2)
        ormask = int(value.replace('X', '0'), 2)
    else:
        pos = int(cmd[4:-1])
        value = (int(value) & andmask) | ormask
        memory[pos] = value
print('one', sum(memory.values()))

def fluctuations(mask, prefix=''):
    if len(mask) == 0:
        return [int(prefix, 2)]
    if mask[0] in '01':
        return fluctuations(mask[1:], prefix+'0')
    else:
        return (fluctuations(mask[1:], prefix+'0')
                + fluctuations(mask[1:], prefix+'1'))

memory = collections.defaultdict(int)
andmask = ormask = flux = None
andmasktrans = str.maketrans('10X', '010')
for cmd, value in data:
    if cmd == 'mask':
        andmask = int(value.translate(andmasktrans), 2) # bits to keep unchanged
        ormask = int(value.replace('X', '0'), 2) # bits to set
        flux = fluctuations(value) # all variants of the floating bits
    else:
        pos = int(cmd[4:-1])
        value = int(value)
        pos = (pos & andmask) | ormask
        for fluc in flux:
            memory[pos|fluc] = value
print('two', sum(memory.values()))
