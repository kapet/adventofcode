import collections

positions = {}
for row, line in enumerate(open('2022/23/input.txt')):
    for col, scan in enumerate(line):
        if scan == '#':
            positions[(row, col)] = None

directions = [
    (0, (-1, 0)),
    (4, (1, 0)),
    (6, (0, -1)),
    (2, (0, 1))
]

round = 0
while True:
    round += 1

    # phase 1: propose a move
    dup_check = collections.Counter()
    for y, x in positions.keys():
        neighbors = [ # NW, N, NE, E, SE, S, SW, W, NW (again)
            (y-1, x-1) in positions,
            (y-1, x) in positions,
            (y-1, x+1) in positions,
            (y, x+1) in positions,
            (y+1, x+1) in positions,
            (y+1, x) in positions,
            (y+1, x-1) in positions,
            (y, x-1) in positions
        ]
        neighbors.append(neighbors[0])

        if not any(neighbors):
            # nothing to do
            pass
        else:
            for d, (dy, dx) in directions:
                if not any(neighbors[d:d+3]):
                    p = (y+dy, x+dx)
                    positions[(y, x)] = p
                    dup_check[p] += 1
                    break
            else:
                positions[(y, x)] = False
    
    # phase 2: move if possible
    any_moved = False
    new_positions = {}
    for current, proposed in positions.items():
        if not proposed or dup_check[proposed] > 1:
            new_positions[current] = False
        else:
            new_positions[proposed] = False
            any_moved = True
    positions = new_positions

    if not any_moved:
        break

    directions.append(directions.pop(0))

    if 0:
        print('----------', round, '-----------')
        for row in range(-5, 15):
            print(''.join([(row, col) in positions and '#' or '.' for col in range(-5, 15)]))

    if round == 10:
        minx = miny = 99
        maxx = maxy = 0
        for (y, x) in positions.keys():
            minx = min(minx, x)
            maxx = max(maxx, x)
            miny = min(miny, y)
            maxy = max(maxy, y)
        print('one:', (maxy-miny+1)*(maxx-minx+1) - len(positions))

print('two:', round)
