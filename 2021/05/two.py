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
    # lines are horizontal, vertical, or 45 degree
    # therefore dx and dy increments are always one of -1,0,1
    # (next step Bresenham lines I guess...)

    # this is like: sign(v2-v1)
    dx = (line.x2 > line.x1) - (line.x2 < line.x1)
    dy = (line.y2 > line.y1) - (line.y2 < line.y1)

    x = line.x1
    y = line.y1
    while True:
        bitmap[y][x] += 1
        if x==line.x2 and y==line.y2:
            # reached the endpoint
            break
        y += dy
        x += dx

for row in bitmap[:10]:
    print(row[:10])

dangerous_areas = 0
for row in bitmap:
    for value in row:
        if value >= 2:
            dangerous_areas += 1

print('found {} dangerous areas'.format(dangerous_areas))