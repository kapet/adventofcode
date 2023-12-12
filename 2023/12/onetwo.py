import functools

records = []
for line in open('2023/12/input.txt'):
    condition, sizes = line.split()
    records.append((condition, tuple(map(int, sizes.split(',')))))


@functools.cache
def arrangements(condition, sizes):
    n = len(condition)
    i = 0
    while i < n:
        if condition[i] == '.':
            # consume good springs
            i += 1
        elif condition[i] == '?':
            # recurse into both options
            return (arrangements('.' + condition[i+1:], sizes)
                    + arrangements('#' + condition[i+1:], sizes))
        else: # condition[i] == '#'
            if not sizes:
                # there should not be any more damaged springs -> fail
                return 0
            size, sizes = sizes[0], sizes[1:]
            if i+size > n or '.' in condition[i:i+size]:
                # not enough damaged springs here -> fail
                return 0
            elif i+size < n and condition[i+size] == '#':
                # there is no undamaged spring after the group -> fail
                return 0
            else:
                # consume groups of damaged springs
                i += size+1
    # reached end of condition string
    # if all sizes have been used up then we found one arrangement
    return 0 if sizes else 1


one = 0
for condition, sizes in records:
    one += arrangements(condition, sizes)
print('one:', one)

expanded_records = []
for condition, sizes in records:
    expanded_records.append(('?'.join([condition]*5), sizes*5))

two = 0
for condition, sizes in expanded_records:
    two += arrangements(condition, sizes)
print('two:', two)
