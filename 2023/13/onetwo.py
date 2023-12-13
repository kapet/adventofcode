patterns = []
pattern = []
for line in open('2023/13/input.txt'):
    line = tuple(line.strip().replace('.', '0').replace('#', '1'))
    if not line:
        patterns.append(pattern)
        pattern = []
    else:
        pattern.append(line)
patterns.append(pattern)

def rotate_cw(pattern):
    return list(zip(*pattern[::-1]))

def rotate_ccw(pattern):
    return list(reversed(list(zip(*pattern))))

# convert rows into numbers, build pairs of rows to compare,
# xor together, count bits, sum -> total number of differences for reflection
def find_reflection_row(pattern, overlap_goal, ignore=0):
    pattern = [int(''.join(line), 2) for line in pattern]
    for i in range(1, len(pattern)):
        n = min(i, len(pattern)-i)
        pairs = zip(pattern[i-n:i], reversed(pattern[i:i+n]))
        overlapped = sum([(a^b).bit_count() for a,b in pairs])
        if overlapped == overlap_goal and i != ignore:
            return i
    return 0

one = 0
two = 0
for pattern in patterns:
    a = find_reflection_row(pattern, 0)
    b = find_reflection_row(pattern, 1, ignore=a)
    one += 100*a
    two += 100*b

    pattern = rotate_cw(pattern)
    a = find_reflection_row(pattern, 0)
    b = find_reflection_row(pattern, 1, ignore=a)
    one += a
    two += b
print('one:', one)
print('two:', two)
