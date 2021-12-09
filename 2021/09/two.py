heightmap = []
for line in open('2021/09/input.txt'):
    line = list(line.strip())
    line = list(map(int, line))
    heightmap.append(line)

minx = miny = 0
maxx = len(heightmap[0])-1
maxy = len(heightmap)-1

def neighbors(x, y):
    result = []
    if y > miny:
        result.append((x, y-1))
    if y < maxy:
        result.append((x, y+1))
    if x > minx:
        result.append((x-1, y))
    if x < maxx:
        result.append((x+1, y))
    return result

low_points = []
for y in range(maxy+1):
    for x in range(maxx+1):
        if all([heightmap[y][x] < heightmap[yn][xn] for xn, yn in neighbors(x, y)]):
            # it's a low point
            low_points.append((x, y))

print('found {} low points'.format(len(low_points)))

floodmap = [[-1]*(maxx+1) for _ in range(maxy+1)]
basins = [[t] for t in low_points]
for i,basin in enumerate(basins):
    # mark the low point itself
    x, y = basin[0]
    floodmap[y][x] = i

    # iterate through the basin, as long as we find and append more fields the loop will continue
    for x, y in basin:
        for nx, ny in neighbors(x, y):
            if floodmap[ny][nx] == -1:
                # field not included in anything
                if heightmap[ny][nx] != 9:
                    basin.append((nx, ny))
                    floodmap[ny][nx] = i
            elif floodmap[ny][nx] == i:
                # field in our own basin, cool
                pass
            else:
                # something went wrong, overflowing into other basin??
                raise Exception('overflow!')

sizes = sorted(map(len, basins), reverse=True)
print('largest 3 basins: {}'.format(sizes[:3]))
print('result = {}'.format(sizes[0]*sizes[1]*sizes[2]))
