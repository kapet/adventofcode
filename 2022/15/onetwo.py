import re

if 0:
    infile = '2022/15/test.txt'
    one_y = 10
    two_max = 20
else:
    infile = '2022/15/input.txt'
    one_y = 2000000
    two_max = 4000000

sensordata = []
m = re.compile(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)$')
for line in open(infile):
    sx,sy,bx,by = map(int, m.match(line).groups())
    distance = abs(sx-bx) + abs(sy-by)
    ystart = sy-distance
    yend = sy+distance
    sensordata.append(((sx,sy),(bx,by),distance,(ystart,yend+1)))

############################# ONE

dest_blocked = []
beacons = set()
for sensor, beacon, distance, yrange in sensordata:
    if beacon[1] == one_y:
        beacons.add(beacon)
    # how many fields on destination line are included
    distancex = distance - abs(sensor[1]-one_y)
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

############################# TWO

for y in range(0, two_max+1):
    if y%100000 == 0:
        print('...', y)

    dest_blocked = []
    for sensor, beacon, distance, yrange in sensordata:
        if y < yrange[0] or y >= yrange[1]:
            continue
        distancex = distance - abs(sensor[1]-y)
        if distancex > 0:
            dest_blocked.append((sensor[0]-distancex, sensor[0]+distancex))

    dest_blocked.sort(key=lambda x: x[0])
    x = 0
    for x0, x1 in dest_blocked:
        if x0 > x:
            # found a hole
            print('found hole at:', x, y)
            print('two:', x*4000000 + y)
            break
        x = max(x, x1+1)
    else:
        # no hole found
        continue
    # found a hole
    break
