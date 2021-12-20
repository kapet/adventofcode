import collections
import itertools
import math

class Vector:
    def __init__(self, iterable):
        self.__value = tuple(iterable)
        assert len(self.__value) == 3
    
    def __eq__(self, other: object) -> bool:
        if type(other) == Vector:
            return self.__value == other.__value
        else:
            return False

    def __hash__(self) -> int:
        return hash(self.__value)

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return 'Vector('+str(self.__value)+')'

    def __add__(self, other):
        if type(other) == Vector:
            return Vector(self.__value[i]+other.__value[i] for i in range(3))
        else:
            raise NotImplemented()

    def __sub__(self, other):
        if type(other) == Vector:
            return Vector(self.__value[i]-other.__value[i] for i in range(3))
        else:
            raise NotImplemented()

    def __abs__(self):
        return Vector(abs(v) for v in self.__value)
    
    def value(self):
        return self.__value

    def length(self):
        return math.sqrt(self.__value[0]**2 + self.__value[1]**2 + self.__value[2]**2)

    def manhattan(self):
        return self.__value[0] + self.__value[1] + self.__value[2]

    def rotate(self, x=0, y=0, z=0):
        val = list(self.__value)
        for _ in range(x):
            val[1], val[2] = -val[2], val[1]
        for _ in range(y):
            val[0], val[2] = -val[2], val[0]
        for _ in range(z):
            val[0], val[1] = -val[1], val[0]
        return Vector(val)

    def all_rotations(self):
        for i,j in ((0,0), (0,1), (0,2), (0,3), (1,0), (1,2)):
            for k in range(4):
                yield (i, j, k)

# parse input file
scanners = []
current_scanner = []
for line in open('2021/19/input.txt'):
    line = line.strip()
    if not line:
        # ignore empty lines
        pass
    elif line.startswith('---'):
        if current_scanner:
            scanners.append(current_scanner)
        current_scanner = []
    else:
        current_scanner.append(Vector(map(int, line.split(','))))
scanners.append(current_scanner)

lengths = [len(t) for t in scanners]
print('got {} scanners, size {}..{}'.format(len(scanners), min(lengths), max(lengths)))

def combine(n):
    # return tuples of coordinates to hit all combinations of two elements in a range of elements
    # such that never an element is combined with itself, no (0, 0) or (1, 1)
    # and that never a pair is returned in reversed order, only (0, 1) but not (1, 0)
    for i in range(0, n-1):
        for j in range(i+1, n):
            yield (i, j)

# calculate relative distances between all beacons for each scanner
beacon_diffs = []
for n, data in enumerate(scanners):
    diffs = collections.defaultdict(list)
    for i, j in combine(len(data)):
        # don't use all_rotations() here, because transitive rotations
        for d in itertools.permutations(abs(data[i]-data[j]).value()):
            diffs[d].append((n, i, j))
    beacon_diffs.append(diffs)

# for each scanner build a set of relative beacon distances,
# then compare all sets with each other for intersections to find likely overlaps
sets = [set(t.keys()) for t in beacon_diffs]
overlaps = []
for i, j in combine(len(sets)):
    overlap = sets[i] & sets[j]
    if len(overlap) < 300:
        # all real overlaps are massive, ignore the occasional noise
        continue
    overlaps.append((i, j, overlap))

# sort all overlaps topologically, starting with scanner 0
sorted_overlaps = []
reached = set([0])
while len(reached) != len(scanners):
    for i, j, overlap in overlaps:
        ir = i in reached
        jr = j in reached
        if ir == jr:
            # both nodes unreachable or already handled, skip
            continue
        elif not jr:
            # know i but not j: i->j
            reached.add(j)
            sorted_overlaps.append((i, j, overlap))
        elif not ir:
            # know j but not i: j->i
            reached.add(i)
            sorted_overlaps.append((j, i, overlap))

# calculate relative positions, starting from scanner 0 by following the topo sort
positions = [None]*len(scanners)
positions[0] = Vector((0, 0, 0))
rotations = [None]*len(scanners)
rotations[0] = [(0, 0, 0)]
for s1, s2, diffpairs in sorted_overlaps:
    # position for s1 is known, need to find s2
    print('looking at {}->{}'.format(s1, s2))

    # verify we have 12 beacons detected on both sides
    src_beacons = set()
    dst_beacons = set()
    for k in diffpairs:
        for t in beacon_diffs[s1][k]:
            src_beacons.add(t[1])
            src_beacons.add(t[2])
        for t in beacon_diffs[s2][k]:
            dst_beacons.add(t[1])
            dst_beacons.add(t[2])
    print('  overlapping beacons: {} and {}'.format(src_beacons, dst_beacons))
    assert len(src_beacons) == 12
    assert len(dst_beacons) == 12

    # sort overlapping beacons so they pair up
    src_beacons = [scanners[s1][t] for t in src_beacons]
    dst_beacons = [scanners[s2][t] for t in dst_beacons]
    src_dist = [[] for _ in range(12)]
    dst_dist = [[] for _ in range(12)]
    for i,j in combine(12):
        dist = (src_beacons[i]-src_beacons[j]).length()
        src_dist[i].append(dist)
        src_dist[j].append(dist)
        dist = (dst_beacons[i]-dst_beacons[j]).length()
        dst_dist[i].append(dist)
        dst_dist[j].append(dist)
    src_dist = [sum(x) for x in src_dist]
    dst_dist = [sum(x) for x in dst_dist]
    src_beacons = [x for _,x in sorted(zip(src_dist, src_beacons))]
    dst_beacons = [x for _,x in sorted(zip(dst_dist, dst_beacons))]

    # take first beacon and calculate offset
    offsets = {}
    for i in range(12):
        b1 = src_beacons[i]
        b2 = dst_beacons[i]
        for rot in b2.all_rotations():
            b2r = b2.rotate(*rot)
            diff = b1-b2r
            offsets.setdefault(diff, []).append(rot)
    offsets = sorted(offsets.items(), key=lambda t: len(t[1]))
    offset, rotation = offsets[-1]
    assert all(t==rotation[0] for t in rotation)
    rotation = rotation[0]
    print('  offset from {} to {} is {}, it is rotated by {}'.format(s1, s2, offset, rotation))

    # the found offset is within the coordinate system of s1
    # the found rotation is how s2 is rotated within s1
    for r in rotations[s1]:
        offset = offset.rotate(*r)
    positions[s2] = positions[s1] + offset
    rotations[s2] = [rotation]+rotations[s1]
    print('  found offset from 0: {}'.format(positions[s2]))

for i in range(len(scanners)):
    print('scanner {} is at {}'.format(i, positions[i]))

# calculate all beacon positions relative to scanner 0
all_beacons = set()
for i in range(len(scanners)):
    for p in scanners[i]:
        for r in rotations[i]:
            p = p.rotate(*r)
        p = positions[i] + p
        all_beacons.add(p)
print('total number of beacons: {}'.format(len(all_beacons)))

# calculate Manhattan distance between all scanners, find max
max_distance = 0
for i,j in combine(len(scanners)):
    d = abs(positions[i] - positions[j]).manhattan()
    if d > max_distance:
        max_distance = d
print('max Manhattan distance between scanners: {}'.format(max_distance))
