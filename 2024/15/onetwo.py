data = open('2024/15/input.txt').read().split('\n\n')
mymap = [list(l) for l in data[0].strip().split('\n')]
h = len(mymap)
w = len(mymap[0])
moves = list(data[1].strip().replace('\n', ''))

def next(y, x, m):
    match m:
        case 'v':
            return (y+1, x)
        case '>':
            return (y, x+1)
        case '<':
            return (y, x-1)
        case '^':
            return (y-1, x)

######################################################## PART 1

for ry in range(h):
    if '@' in mymap[ry]:
        rx = mymap[ry].index('@')
        break
mymap[ry][rx] = '.'

def push(y, x, m):
    match mymap[y][x]:
        case '.':
            return True
        case '#':
            return False
        case 'O':
            ny, nx = next(y, x, m)
            if push(ny, nx, m):
                mymap[ny][nx] = mymap[y][x]
                mymap[y][x] = '.'
                return True
            else:
                return False
        case _:
            raise Exception('bad map content:', y, x, mymap[y][x])

for m in moves:
    ny, nx = next(ry, rx, m)
    if push(ny, nx, m):
        assert mymap[ry][rx] == '.'
        ry, rx = ny, nx

one = 0
for y in range(h):
    for x in range(w):
        if mymap[y][x] == 'O':
            one += y*100 + x
print('one', one)

######################################################## PART 2

mymap = []
for l in data[0].strip().split('\n'):
    l = l.replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.')
    mymap.append(list(l))
h = len(mymap)
w = len(mymap[0])

for ry in range(h):
    if '@' in mymap[ry]:
        rx = mymap[ry].index('@')
        break
mymap[ry][rx] = '.'

def push2(y, x, m):
    match (mymap[y][x], m):
        case ('.', _):
            return True
        case ('#', _):
            return False
        case (_, '<') | (_, '>'):
            ny, nx = next(y, x, m)
            if push2(ny, nx, m):
                mymap[ny][nx] = mymap[y][x]
                mymap[y][x] = '.'
                return True
            else:
                return False
        case ('[', _):
            ny, nx = next(y, x, m)
            if push2(ny, nx, m) and push2(ny, nx+1, m):
                mymap[ny][nx] = mymap[y][x]
                mymap[ny][nx+1] = mymap[y][x+1]
                mymap[y][x] = '.'
                mymap[y][x+1] = '.'
                return True
            else:
                return False
        case (']', _):
            ny, nx = next(y, x, m)
            if push2(ny, nx-1, m) and push2(ny, nx, m):
                mymap[ny][nx-1] = mymap[y][x-1]
                mymap[ny][nx] = mymap[y][x]
                mymap[y][x-1] = '.'
                mymap[y][x] = '.'
                return True
            else:
                return False

for m in moves:
    ny, nx = next(ry, rx, m)
    old_map = [l[:] for l in mymap]
    if push2(ny, nx, m):
        assert mymap[ny][nx] == '.'
        ry, rx = ny, nx
    else:
        mymap = old_map

two = 0
for y in range(h):
    for x in range(w):
        if mymap[y][x] == '[':
            two += y*100 + x
print('two', two)
