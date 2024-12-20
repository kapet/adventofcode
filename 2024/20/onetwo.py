mymap = [list(l.strip()) for l in open('2024/20/input.txt')]
w = len(mymap[0])
h = len(mymap)

for y in range(h):
    for x in range(w):
        if mymap[y][x] == 'S':
            sy, sx = y, x
        elif mymap[y][x] == 'E':
            ey, ex = y, x
mymap[ey][ex] = '.'

y, x, d = sy, sx, 1
distances = [[0]*w for _ in range(h)]
path = []
while (y,x) != (ey,ex):
    distances[y][x] = d
    path.append((y,x))
    for dy, dx in [(-1,0), (1,0), (0,1), (0,-1)]:
        ny, nx = y+dy, x+dx
        if 0 <= ny < h and 0 <= nx < w and mymap[ny][nx] == '.' and not distances[ny][nx]:
            y, x, d = ny, nx, d+1
            break
distances[y][x] = d
path.append((y,x))

def find_shorts(maxd, minsavings):
    shorts = 0
    for i, (y,x) in enumerate(path, start=1):
        for ny in range(y-maxd, y+1+maxd):
            for nx in range(x-maxd, x+1+maxd):
                if 0 <= ny < w and 0 <= nx < h:
                    d = abs(ny-y) + abs(nx-x)
                    if 0 < d <= maxd:
                        s = distances[ny][nx] - i - d
                        if s >= minsavings:
                            shorts += 1
    return shorts

print('one', find_shorts(2, 100))
print('two', find_shorts(20, 100))
