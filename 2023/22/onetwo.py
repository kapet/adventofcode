import collections
import itertools

bricks = []
for line in open('2023/22/input.txt'):
    coords = tuple(map(int, line.replace('~', ',').split(',')))
    bricks.append((coords[:3], coords[3:]))

# coordinates are (x,y,z)
# x and y are 0..2 for the test and 0..9 for the input
# z is 1..9 for the test and 1..341 for the input

# figure out size of stack in every direction
mins = list(bricks[0][0])
maxs = mins[:]
for pos in bricks:
    for p in pos:
        for i,a in enumerate(p):
            mins[i] = min(mins[i], a)
            maxs[i] = max(maxs[i], a)
assert mins[0] == mins[1] == 0
sizex = maxs[0] + 1
sizey = maxs[1] + 1
sizez = maxs[2] - mins[2] + 1

# sort bricks by elevation, lowest first
bricks.sort(key=lambda t: min(t[0][2], t[1][2]))

def absrange(p0, p1):
    if p0 > p1:
        p0,p1 = p1,p0
    return range(p0, p1+1)

# drop all bricks down until they touch the ground (or previously dropped bricks)
# heightmap is a 2d map giving the height above ground
# occupymap is a 3d map storing the id+1 of the brick occupying that space
occupymap = [[[0]*sizex for _ in range(sizey)] for _ in range(sizez)]
heightmap = [[0]*sizex for _ in range(sizey)]
for i, (start, end) in enumerate(bricks, start=1):
    coords = list(itertools.product(absrange(start[0], end[0]), absrange(start[1], end[1])))
    floor = max(heightmap[y][x] for x,y in coords)
    ext = abs(start[2]-end[2]) + 1
    for x,y in coords:
        heightmap[y][x] = floor + ext
        for z in range(floor, floor+ext):
            assert occupymap[z][y][x] == 0
            occupymap[z][y][x] = i

# figure out which bricks support each other
supports_up = collections.defaultdict(set)
supports_down = collections.defaultdict(set)
for z in range(sizez-1):
    for y in range(sizey):
        for x in range(sizex):
            here = occupymap[z][y][x]
            above = occupymap[z+1][y][x]
            if here and above and here != above:
                supports_up[here-1].add(above-1)
                supports_down[above-1].add(here-1)

# for task one count all bricks that do NOT have bricks above them that have no other supports
has_single_support = set(i for i in range(len(bricks)) if len(supports_down[i]) < 2)
number_of_singles_above = collections.Counter()
for here, above in supports_up.items():
    for a in above:
        if a in has_single_support:
            number_of_singles_above[here] += 1
print('one:', len(bricks) - len(number_of_singles_above))

# for task two the problem is 'multiple inheritance': a brick can be supported by two bricks,
# which in turn are supported by the same brick below. If the lowest brick is removed, all of
# them drop, despite some having multiple supports!
# Use a 'reverse mark and sweep' algorithmus to first mark all bricks on top of the brick to remove,
# then in a second step un-mark all bricks having other supports outside of this 'stack'.
two = 0
for i in range(len(bricks)):
    mark = [0]*len(bricks)

    # step 1: mark all bricks on top of 'i'
    heap = set((i,))
    while heap:
        p = heap.pop()
        if not mark[p]:
            mark[p] = 1
            heap.update(supports_up[p])

    # step 2: unmark all bricks on top of unmarked bricks
    heap = set(i for i in range(len(bricks)) if not mark[i])
    while heap:
        p = heap.pop()
        if p == i:
            continue
        mark[p] = 0
        heap.update(supports_up[p])

    two += sum(mark) - 1
print('two:', two)
