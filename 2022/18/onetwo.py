cubes = set()
for line in open('2022/18/input.txt'):
    pos = tuple([int(t) for t in line.strip().split(',')])
    cubes.add(pos)

total = 0
for x,y,z in cubes:
    for d in (-1, 1):
        if (x+d, y, z) not in cubes:
            total += 1
        if (x, y+d, z) not in cubes:
            total += 1
        if (x, y, z+d) not in cubes:
            total += 1
print('one:', total)

minx, miny, minz = maxx, maxy, maxz = None, None, None
for x,y,z in cubes:
    if minx is None:
        minx, miny, minz = maxx, maxy, maxz = x, y, z
    else:
        minx = min(minx, x)
        maxx = max(maxx, x)
        miny = min(miny, y)
        maxy = max(maxy, y)
        minz = min(minz, z)
        maxz = max(maxz, z)

minx -= 1
miny -= 1
minz -= 1
maxx += 1
maxy += 1
maxz += 1

stack = [(minx, miny, minz)]
steam = set(stack)
steps = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
while stack:
    x,y,z = stack.pop(0)
    for stepx,stepy,stepz in steps:
        nx,ny,nz = x+stepx, y+stepy, z+stepz
        if (nx >= minx and nx <= maxx
                and ny >= miny and ny <= maxy
                and nz >= minz and nz <= maxz
                and (nx,ny,nz) not in cubes
                and (nx,ny,nz) not in steam):
            steam.add((nx,ny,nz))
            stack.append((nx,ny,nz))

total = 0
for x,y,z in cubes:
    for d in (-1, 1):
        if (x+d, y, z) in steam:
            total += 1
        if (x, y+d, z) in steam:
            total += 1
        if (x, y, z+d) in steam:
            total += 1
print('two:', total)
