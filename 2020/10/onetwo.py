import collections
import functools

# each adapter is unique, get them in sorted order
adapters = list(sorted(int(l) for l in open('2020/10/input.txt')))
device = max(adapters) + 3

# all adapters must be used -> get all neighbor differences
one = [0] + adapters + [device]
diffs = collections.Counter(b-a for a,b in zip(one, one[1:]))
print('one', diffs[1]*diffs[3])

# many different paths but always the same number from a specific
# position, so just cache them to avoid repeated recursion
@functools.cache
def ways(position):
    if position + 3 == device:
        return 1
    result = 0
    for a in adapters:
        if 1 <= (a-position) <= 3:
            result += ways(a)
    return result
print('two', ways(0))
