import re

steps = []
parser_re = re.compile(r'([onf]*) x=(-?\d*)\.\.(-?\d*),y=(-?\d*)\.\.(-?\d*),z=(-?\d*)\.\.(-?\d*)')
for line in open('2021/22/input.txt'):
    match = parser_re.fullmatch(line.strip())
    groups = list(match.groups())
    groups[0] = groups[0] == 'on'
    for i in range(1, 7):
        groups[i] = int(groups[i])
    steps.append(groups)

# 100*100*100 = 1M elements, not too much for a simple grid
grid = [[[False]*101 for _ in range(101)] for _ in range(101)]
for target_state, xmin, xmax, ymin, ymax, zmin, zmax in steps:
    for x in range(xmin, xmax+1):
        if x < -50 or x > 50:
            continue
        for y in range(ymin, ymax+1):
            if y < -50 or y > 50:
                continue
            for z in range(zmin, zmax+1):
                if z < -50 or z > 50:
                    continue
                grid[x+50][y+50][z+50] = target_state

total = 0
for x in grid:
    for y in x:
        total += sum(y)
print(total)

# expect sparse results, store in dict: grid[(x,y,z)] = True/False
grid = {}

for target_state, xmin, xmax, ymin, ymax, zmin, zmax in steps:
    for x in range(xmin, xmax+1):
        if x < -50 or x > 50:
            continue
        for y in range(ymin, ymax+1):
            if y < -50 or y > 50:
                continue
            for z in range(zmin, zmax+1):
                if z < -50 or z > 50:
                    continue
                grid[(x,y,z)] = target_state

print(sum(grid.values()))