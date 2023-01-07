# part 2 was surprisingly difficult, or I just didn't recognize a simpler way :-(
# I have used two little paper cubes to build intuition, and a graph of relationships
# between the sides. But eventually I decided to just manually solve the inter-side
# relationship and hardcode it in the table below and call it a day.

data_test = [
    '2022/22/test.txt',
    4,
    # (rotate, row, column)
    ((2, 0, 2), (1, 0, 2), (2, 1, 0), (-1, 1, 2)),  # up
    ((2, 2, 2), (-1, 2, 2), (2, 1, 0), (-1, 1, 0)),  # down
    ((-1, 1, 1), (1, 2, 3), (1, 1, 1)),  # left
    ((2, 2, 3), (1, 2, 3), (2, 0, 2)),  # right
]
data_input = [
    '2022/22/input.txt',
    50,
    # (rotate, row, column)
    ((1, 1, 1), (1, 3, 0), (0, 3, 0)),  # up
    ((0, 0, 2), (1, 3, 0), (1, 1, 1)),  # down
    ((2, 2, 0), (-1, 2, 0), (2, 0, 1), (-1, 0, 1)),  # left
    ((2, 2, 1), (-1, 0, 2), (2, 0, 2), (-1, 2, 1)),  # right
]
data_inputsmall = [
    '2022/22/input_small.txt',
    5,
    # (rotate, row, column)
    ((1, 1, 1), (1, 3, 0), (0, 3, 0)),  # up
    ((0, 0, 2), (1, 3, 0), (1, 1, 1)),  # down
    ((2, 2, 0), (-1, 2, 0), (2, 0, 1), (-1, 0, 1)),  # left
    ((2, 2, 1), (-1, 0, 2), (2, 0, 2), (-1, 2, 1)),  # right
]

data = data_input

filedata = [l.rstrip() for l in open(data[0])]
map_ = filedata[0:-2]
path_ = filedata[-1]

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
        start_position = (0, i)
        start_direction = (0, 1)
        break
else:
    raise Exception()

clockwise = [(0, 1), (1, 0), (0, -1), (-1, 0)]
map_ = [list(t) for t in map_]

############################################# ONE

position, direction = start_position, start_direction
path_data = list(path_)
while path_data:
    if path_data[0] in 'RL':
        turn = (path_data.pop(0) == 'R') and 1 or -1
        direction = clockwise[(clockwise.index(direction) + turn + 4) % 4]
    else:
        n = ''
        while path_data and path_data[0].isdecimal():
            n += path_data.pop(0)
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

row = position[0]+1
column = position[1]+1
facing = clockwise.index(direction)
print('one:', row, column, facing, '->', 1000*row+4*column+facing)

############################################# ONE

edge = data[1]

jumps_vert = {}
for x in range(max(row_max)+1):
    block, pos = divmod(x, edge)

    # going up
    target_rot, target_row, target_col = data[2][block]
    ty = target_row * edge
    tx = target_col * edge
    if target_rot == 0:
        ty += edge-1
        tx += pos
    elif target_rot == 2:
        tx += edge-1 - pos
    elif target_rot == 1:
        ty += pos
    elif target_rot == -1:
        ty += edge-1 - pos
        tx += edge-1
    else:
        raise Exception()
    jumps_vert[(col_min[x]-1, x)] = (target_rot, ty, tx)

    # going down
    target_rot, target_row, target_col = data[3][block]
    ty = target_row * edge
    tx = target_col * edge
    if target_rot == 0:
        tx += pos
    elif target_rot == 2:
        ty += edge-1
        tx += edge-1 - pos
    elif target_rot == 1:
        ty += pos
        tx += edge-1
    elif target_rot == -1:
        ty += edge-1 - pos
    else:
        raise Exception()
    jumps_vert[(col_max[x]+1, x)] = (target_rot, ty, tx)

jumps_horiz = {}
for y in range(max(col_max)+1):
    block, pos = divmod(y, edge)

    # going left
    target_rot, target_row, target_col = data[4][block]
    ty = target_row * edge
    tx = target_col * edge
    if target_rot == 0:
        ty += pos
        tx += edge-1
    elif target_rot == 2:
        ty += edge-1 - pos
    elif target_rot == 1:
        ty += edge-1
        tx += edge-1 - pos
    elif target_rot == -1:
        tx += pos
    else:
        raise Exception()
    jumps_horiz[(y, row_min[y]-1)] = (target_rot, ty, tx)

    # going right
    target_rot, target_row, target_col = data[5][block]
    ty = target_row * edge
    tx = target_col * edge
    if target_rot == 0:
        ty += pos
    elif target_rot == 2:
        ty += edge-1 - pos
        tx += edge-1
    elif target_rot == 1:
        tx += edge-1 - pos
    elif target_rot == -1:
        ty += edge-1
        tx += pos
    else:
        raise Exception()
    jumps_horiz[(y, row_max[y]+1)] = (target_rot, ty, tx)

do_print_progress = False
print_map = [t.copy() for t in map_]
direction_char = '>v<^'

position, direction = start_position, start_direction
path_data = list(path_)
while path_data:
    if path_data[0] in 'RL':
        if do_print_progress:
            print('turn', path_data[0])
        turn = (path_data.pop(0) == 'R') and 1 or -1
        direction = clockwise[(clockwise.index(direction) + turn + 4) % 4]
    else:
        n = ''
        while path_data and path_data[0].isdecimal():
            n += path_data.pop(0)
        n = int(n)
        if do_print_progress:
            print('forward', n)
        for _ in range(n):
            y, x = position
            print_map[y][x] = direction_char[clockwise.index(direction)]
            if direction[0]:
                y += direction[0]
                jump = jumps_vert.get((y,x), None)
            else:
                x += direction[1]
                jump = jumps_horiz.get((y,x), None)
            if jump:
                rot, y, x = jump
                tmp_direction = clockwise[(clockwise.index(direction) + rot + 4) % 4]
            else:
                tmp_direction = direction
            if map_[y][x] == '.':
                # open tile
                position = (y, x)
                direction = tmp_direction
            elif map_[y][x] == '#':
                break
            else:
                print(y, x, map_[y][x])
                raise Exception()

        if do_print_progress:
            for l in print_map:
                print(''.join(l))
            print()

row = position[0]+1
column = position[1]+1
facing = clockwise.index(direction)
print('two:', row, column, facing, '->', 1000*row+4*column+facing)
