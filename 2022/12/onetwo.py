start = end = None
map_ = []
row = 0
for line in open('input.txt'):
    if 'S' in line:
        start = (row, line.find('S'))
        line = line.replace('S', 'a')
    if 'E' in line:
        end = (row, line.find('E'))
        line = line.replace('E', 'z')
    map_.append([ord(t)-ord('a') for t in line.strip()])
    row += 1

h = len(map_)
w = len(map_[0])

def findPath(start_):
    distance_map = [[9999999]*w for _ in range(h)]
    distance_map[start_[0]][start_[1]] = 0
    active = [(start_, 0)]
    while active:
        (y, x), steps = active.pop(0)
        for ny, nx in [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]:
            if ny < 0 or ny >= h or nx < 0 or nx >= w:
                # outside of map -> ignore
                continue
            if map_[ny][nx] > map_[y][x]+1:
                # more than one step higher -> ignore
                continue
            if distance_map[ny][nx] <= steps+1:
                # already found another shorter path -> ignore
                continue
            # this is a new shortest path to this field!
            distance_map[ny][nx] = steps+1
            active.append(((ny, nx), steps+1))
    return distance_map[end[0]][end[1]]

print('one:', findPath(start))

min_distance = 9999999
for y in range(h):
    for x in range(w):
        if map_[y][x] == 0:
            d = findPath((y, x))
            if d < min_distance:
                min_distance = d

print('two:', min_distance)
