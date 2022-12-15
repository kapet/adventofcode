import re

minx=miny=maxx=maxy = None
sensordata = []
m = re.compile(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)$')
for line in open('2022/15/input.txt'):
    sx,sy,bx,by = map(int, m.match(line).groups())
    sensordata.append(((sx,sy),(bx,by)))
    if minx == None:
        minx,miny,maxx,maxy = sx,sy,sx,sy
    for x in (sx, bx):
        minx = min(minx, x)
        maxx = max(maxx, x)
    for y in (sy, by):
        miny = min(miny, y)
        maxy = max(maxy, y)

if 0:
    map_ = [['.']*60 for _ in range(60)]
    i = 0
    for sensor, beacon in sensordata:
        distancey = abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1])
        for y in range(sensor[1]-distancey, sensor[1]+distancey+1):
            distancex = distancey - abs(sensor[1]-y)
            for x in range(sensor[0]-distancex, sensor[0]+distancex+1):
                if map_[y+30][x+30] not in 'SB':
                    map_[y+30][x+30] = chr(97+i)
        map_[sensor[1]+30][sensor[0]+30] = 'S'
        map_[beacon[1]+30][beacon[0]+30] = 'B'
        i += 1
    print('                 1    1    2    2')
    print('       0    5    0    5    0    5')
    for i, line in enumerate(map_[30:]):
        print('{:2} {}'.format(i, ''.join(line[26:])))

dest_blocked = []
beacons = set()
y = 2000000
for sensor, beacon in sensordata:
    if beacon[1] == y:
        beacons.add(beacon)
    # steps to beacon
    distancey = abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1])
    # how many fields on destination line are included
    distancex = distancey - abs(sensor[1]-y)
    if distancex > 0:
        # sensor field overlaps destination line
        dest_blocked.append((sensor[0]-distancex, sensor[0]+distancex))

dest_blocked.sort(key=lambda x: x[0])
count = dest_blocked[0][1] - dest_blocked[0][0] + 1
until = dest_blocked[0][1]
for x0, x1 in dest_blocked[1:]:
    if x1 <= until:
        # already completely covered
        continue
    # skip overlaps
    x0 = max(x0, until+1)
    count += x1-x0+1
    until = x1

print('one:', count-len(beacons))

