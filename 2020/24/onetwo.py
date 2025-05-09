lines = []
for l in open('2020/24/input.txt'):
    l = l.strip()
    line = []
    i = 0
    while i < len(l):
        if l[i] in 'ew':
            line.append(l[i])
            i += 1
        else:
            line.append(l[i:i+2])
            i += 2
    lines.append(line)

# 24: 23  24  25  26  27
# 25:   23  24  25  26
# 26: 23  24  25  26  27

width = 150
positions = []
floor = [[0] * width for _ in range(width)]
midx = midy = width//2
for line in lines:
    x, y = midx, midy
    for step in line:
        odd = (y % 2) and True or False
        if step == 'e':
            x += 1
        elif step == 'w':
            x -= 1
        elif step == 'ne':
            x += odd and 1 or 0
            y -= 1
        elif step == 'nw':
            x -= (not odd) and 1 or 0
            y -= 1
        elif step == 'se':
            x += odd and 1 or 0
            y += 1
        elif step == 'sw':
            x -= (not odd) and 1 or 0
            y += 1
        else:
            raise Exception()
    positions.append((x, y))
    floor[y][x] = 1 - floor[y][x]

unique_positions = set(positions)
duplicates = len(positions) - len(unique_positions)
print('one', len(unique_positions) - duplicates)

def printfloor(floor):
    for i, l in enumerate(floor):
        if i % 2:
            prefix = ' '
        else:
            prefix = ''
        print(f'{i:2}', prefix, ' '.join(t and '#' or '.' for t in l))

printfloor(floor)

for day in range(100):
    nextfloor = [[0]*width for l in floor]
    for y in range(1, len(floor)-1):
        for x in range(1, len(floor[y])-1):
            if y % 2:
                neighbors = (
                    floor[y][x-1],
                    floor[y][x+1],
                    floor[y-1][x+1],
                    floor[y-1][x],
                    floor[y+1][x+1],
                    floor[y+1][x],
                )
            else:
                neighbors = (
                    floor[y][x-1],
                    floor[y][x+1],
                    floor[y-1][x],
                    floor[y-1][x-1],
                    floor[y+1][x],
                    floor[y+1][x-1],
                )
            n = sum(neighbors)
            #print('   ', y, x, floor[y][x], n)
            if floor[y][x] == 1:
                if n == 0 or n > 2:
                    nextfloor[y][x] = 0
                else:
                    nextfloor[y][x] = 1
            else:
                if n == 2:
                    nextfloor[y][x] = 1
                else:
                    nextfloor[y][x] = 0
    floor = nextfloor
    print(day+1, sum(sum(l) for l in floor))
    #printfloor(floor)

