mymap = [list(l.strip()) for l in open('2020/11/input.txt')]
w = len(mymap[0])
h = len(mymap)

def occupied(data, addresses):
    return [data[y][x] for y,x in addresses].count('#')

def direct_neighbors(y, x):
    result = []
    for yy in range(y-1, y+2):
        for xx in range(x-1, x+2):
            if 0 <= yy < h and 0 <= xx < w and not (yy==y and xx==x):
                result.append((yy, xx))
    return result

def visible_neighbors(y, x):
    result = []
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if dx == dy == 0:
                continue
            ny, nx = y+dy, x+dx
            while 0 <= ny < h and 0 <= nx < w:
                if mymap[ny][nx] != '.':
                    result.append((ny, nx))
                    break
                ny += dy
                nx += dx
    return result

def run(currentmap, lookup, limit):
    modified = True
    while modified:
        newmap = [l[:] for l in currentmap]
        modified = False
        for y in range(h):
            for x in range(w):
                m = currentmap[y][x]
                if m == '.':
                    continue
                n = occupied(currentmap, lookup[(y,x)])
                if m == 'L' and n == 0:
                    newmap[y][x] = '#'
                    modified = True
                elif m == '#' and n >= limit:
                    newmap[y][x] = 'L'
                    modified = True
        currentmap = newmap
    return sum(l.count('#') for l in currentmap)

lookup = {}
for y in range(h):
    for x in range(w):
        lookup[(y,x)] = direct_neighbors(y, x)
print('one', run(mymap, lookup, 4))

lookup = {}
for y in range(h):
    for x in range(w):
        lookup[(y,x)] = visible_neighbors(y, x)
print('two', run(mymap, lookup, 5))
