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
        
print(total)
