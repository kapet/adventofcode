# walk normally
#   track direction of visit for every field
#   only try setting boxes on empty fields in front (and not on start)
#   walk new path
#     until stepping outside bounds -> no loop
#     until hitting an already visited path in same direction -> loop

map_ = [list(l.strip()) for l in open('2024/06/input.txt')]
h = len(map_)
w = len(map_[0])

for sy, l in enumerate(map_):
    if '^' in l:
        sx = l.index('^')
        break

DIR = {
    '^': [-1, 0, '>'],
    '>': [ 0, 1, 'v'],
    'v': [ 1, 0, '<'],
    '<': [ 0,-1, '^'],
}

class FoundEnd(Exception):
    pass

def next_step(mymap, y, x, d):
    # find next free field ahead
    while True:
        dy, dx, tr = DIR[d]
        ny, nx = y+dy, x+dx
        if ny < 0 or ny >= h or nx < 0 or nx >= w:
            # stepped off the field
            raise FoundEnd()
        c = mymap[ny][nx]
        if c == '#':
            # path is blocked, turn right without moving
            d = tr
        else:
            # ok to move forward
            return ny, nx, d

def check_loop(mymap, y, x, d):
    while True:
        if mymap[y][x] == d:
           # been here before, must be a loop
           return True
        mymap[y][x] = d
        try:
            y, x, d = next_step(mymap, y, x, d)
        except FoundEnd:
            # stepped off the grid, so no loop found
            return False

def find_loops(mymap, y, x, d):
    loops = set()
    try:
        while True:
            mymap[y][x] = d
            ny, nx, nd = next_step(mymap, y, x, d)

            if mymap[ny][nx] == '.':
                # next field is empty, try blocking it and see if that creates a loop
                testmap = [l[:] for l in mymap]
                testmap[ny][nx] = '#'
                if check_loop(testmap, y, x, DIR[nd][2]):
                    loops.add((ny,nx))

            y, x, d = ny, nx, nd
    except FoundEnd:
        return loops

loops = find_loops(map_, sy, sx, '^')
print('one', sum(sum(1 for c in l if c in DIR) for l in map_))
print('two', len(loops))
