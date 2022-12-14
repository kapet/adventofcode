class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
    
    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)

    def getIncrementTowards(self, other):
        x = (self.x < other.x) - (self.x > other.x)
        y = (self.y < other.y) - (self.y > other.y)
        return Point(x, y)

maxy = 0
paths = []
for line in open('2022/14/input.txt'):
    path = []
    for point in line.strip().split(' -> '):
        path.append(Point(*point.split(',')))
        maxy = max(maxy, path[-1].y)
    paths.append(path)

#################### ONE

map_ = {}
map_[Point(500, 0)] = '+'
for path in paths:
    for i in range(len(path)-1):
        p0, p1 = path[i], path[i+1]
        inc = p0.getIncrementTowards(p1)
        map_[p0] = '#'
        while p0 != p1:
            p0 = p0 + inc
            map_[p0] = '#'

sand_movements = [Point(0, 1), Point(-1, 1), Point(1, 1)]
total_sand = 0
sand_lost = False
while not sand_lost:
    sand = Point(500, 0)
    moved = True
    while moved:
        moved = False
        for movement in sand_movements:
            sand_moved = sand + movement
            if map_.get(sand_moved, '.') == '.':
                sand = sand_moved
                moved = True
                break
        if sand.y > maxy:
            sand_lost = True
            break
    map_[sand] = 'o'
    total_sand += 1

print('one:', total_sand-1)

#################### TWO

map_ = {}
map_[Point(500, 0)] = '+'
for path in paths:
    for i in range(len(path)-1):
        p0, p1 = path[i], path[i+1]
        inc = p0.getIncrementTowards(p1)
        map_[p0] = '#'
        while p0 != p1:
            p0 = p0 + inc
            map_[p0] = '#'

sand_movements = [Point(0, 1), Point(-1, 1), Point(1, 1)]
total_sand = 0
while True:
    sand = Point(500, 0)
    moved = True
    while moved:
        moved = False
        for movement in sand_movements:
            sand_moved = sand + movement
            if map_.get(sand_moved, '.') == '.':
                sand = sand_moved
                moved = True
                break
        if sand.y > maxy:
            break
    map_[sand] = 'o'
    total_sand += 1
    if sand == Point(500, 0):
        break

print('two:', total_sand)


if 0:
    print()
    for y in range(15):
        line = []
        for x in range(490, 510):
            p = Point(x, y)
            line.append(map_.get(p, '.'))
        print(''.join(line))

