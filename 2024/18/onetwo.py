data = [list(map(int, l.split(','))) for l in open('2024/18/input.txt')]
if len(data) < 50:
    hw = 7
    n = 12
else:
    hw = 71
    n = 1024

def drop(n):
    mymap = [['.'] * hw for _ in range(hw)]
    for x, y in data[:n]:
        mymap[y][x] = '#'
    return mymap

DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def trace(mymap):
    stack = [(0, 0, 0)]
    distance = {}
    while stack:
        x, y, d = stack.pop(0)

        if (y,x) in distance and distance[(y, x)] <= d:
            continue
        distance[(y, x)] = d

        for dx, dy in DIRECTIONS:
            nx, ny, nd = x+dx, y+dy, d+1
            if 0 <= nx < hw and 0 <= ny < hw and mymap[y][x] == '.':
                stack.append((nx, ny, nd))
    return distance.get((hw-1, hw-1))

mapone = drop(n)
print('one', trace(mapone))

low = 0
high = len(data)
while low < high-1:
    mid = (low + high) // 2
    if trace(drop(mid)) == None:
        high = mid
    else:
        low = mid
print('two', data[low])
