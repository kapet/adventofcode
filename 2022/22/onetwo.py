data = [l.rstrip() for l in open('2022/22/input.txt')]
map_ = data[0:-2]
path_ = data[-1]
del data

clockwise = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# find min and max indexes for each row and column
row_min = []
row_max = []
for row in map_:
    total = len(row)
    stripped = len(row.lstrip())
    row_min.append(total-stripped)
    row_max.append(total-1)

col_min = []
col_max = []
for x in range(0, max(row_max)+1):
    for y in range(len(map_)):
        if x < len(map_[y]) and map_[y][x] in '.#':
            break
    else:
        y = None
    col_min.append(y)

    for y in range(len(map_)-1, -1, -1):
        if x < len(map_[y]) and map_[y][x] in '.#':
            break
    else:
        y = None
    col_max.append(y)

# find start position
for i in range(len(map_[0])):
    if map_[0][i] == '.':
        position = (0, i)
        direction = (0, 1)
        break
else:
    raise Exception()

map_ = [list(t) for t in map_]
path_ = list(path_)
while path_:
    if path_[0] in 'RL':
        turn = (path_.pop(0) == 'R') and 1 or -1
        direction = clockwise[(clockwise.index(direction) + turn + 4) % 4]
    else:
        n = ''
        while path_ and path_[0].isdecimal():
            n += path_.pop(0)
        n = int(n)
        for _ in range(n):
            y, x = position
            if direction[0]:
                y += direction[0]
                if y > col_max[x]:
                    y = col_min[x]
                elif y < col_min[x]:
                    y = col_max[x]
            else:
                x += direction[1]
                if x > row_max[y]:
                    x = row_min[y]
                elif x < row_min[y]:
                    x = row_max[y]
            if map_[y][x] == '.':
                # open tile
                #map_[y][x] = 'O'
                position = (y, x)
            elif map_[y][x] == '#':
                break
            else:
                print(y, x, map_[y][x])
                raise Exception()

if 0:
    for l in map_:
        print(''.join(l))

row = position[0]+1
column = position[1]+1
facing = clockwise.index(direction)
print('one:', row, column, facing, '->', 1000*row+4*column+facing)
