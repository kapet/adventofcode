sequence = open('2023/15/input.txt').read().strip().split(',')

def hash_(s):
    current = 0
    for c in s:
        current += ord(c)
        current = (current * 17) & 0xff
    return current

one = 0
box_lenses = [[] for _ in range(256)]
box_flengths = [[] for _ in range(256)]
for line in sequence:
    one += hash_(line)

    if '=' in line:
        lens, flen = line.split('=')
        box = hash_(lens)
        if lens in box_lenses[box]:
            i = box_lenses[box].index(lens)
            box_lenses[box][i] = lens
            box_flengths[box][i] = flen
        else:
            box_lenses[box].append(lens)
            box_flengths[box].append(flen)
    else:
        lens = line[:-1]
        box = hash_(lens)
        if lens in box_lenses[box]:
            i = box_lenses[box].index(lens)
            del box_lenses[box][i], box_flengths[box][i]

print('one:', one)

two=0
for i in range(256):
    for pos, flen in enumerate(box_flengths[i], start=1):
        two += (i+1)*pos*int(flen)
print('two:', two)