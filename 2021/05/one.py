import collections

Line = collections.namedtuple('Line', ['x1', 'y1', 'x2', 'y2'])

lines = []
for l in open('2021/05/input.txt'):
    src, _, dest = l.split()
    lines.append(Line(*(int(i) for i in src.split(',')+dest.split(','))))
print('got {} lines'.format(len(lines)))

# test set is 0..9 for x and y
# input set is 10..990 for x and y
# 1000*1000 is 1M, what's a few MB between friends...?

bitmap = [[0]*1000 for _ in range(1000)]

for line in lines:
    if line.y1 == line.y2:
        # horizontal line
        y = line.y1
        x1 = min(line.x1, line.x2)
        x2 = max(line.x1, line.x2)
        for x in range(x1, x2+1):
            bitmap[y][x] += 1

    elif line.x1 == line.x2:
        # vertical line
        x = line.x1
        y1 = min(line.y1, line.y2)
        y2 = max(line.y1, line.y2)
        for y in range(y1, y2+1):
            bitmap[y][x] += 1

    else:
        # diagonal line
        pass

for row in bitmap[:10]:
    print(row[:10])

dangerous_areas = 0
for row in bitmap:
    for value in row:
        if value >= 2:
            dangerous_areas += 1

print('found {} dangerous areas'.format(dangerous_areas))