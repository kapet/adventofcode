def parse(l):
    return [(e[0], int(e[1:])) for e in l.split(',')]

l1, l2 = map(parse, open("2019/03/input.txt").read().strip().split('\n'))

def trace(l):
    x = y = 0
    steps = 0
    locations = {}
    for direction, n in l:
        for i in range(n):
            if direction == 'R':
                x += 1
            elif direction == 'L':
                x -= 1
            elif direction == 'U':
                y -= 1
            elif direction == 'D':
                y += 1
            else:
                raise Exception()
            steps += 1
            if (x, y) not in locations:
                locations[(x, y)] = steps
    return locations

loc1 = trace(l1)
loc2 = trace(l2)

pos1 = set(loc1.keys())
pos2 = set(loc2.keys())
intersections = pos1.intersection(pos2)
one = 1000000000
two = 1000000000
for x, y in intersections:
    one = min(one, abs(x)+abs(y))
    two = min(two, loc1[(x,y)] + loc2[(x,y)])
print('one', one)
print('two', two)
