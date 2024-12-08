import itertools

map_ = [list(l.strip()) for l in open('2024/08/input.txt')]
w = len(map_[0])
h = len(map_)

antennas = {}
for y in range(h):
    for x in range(w):
        if map_[y][x] != '.':
            antennas.setdefault(map_[y][x], []).append((y,x))

antinodes = set()
for freq, positions in antennas.items():
    for (y1, x1), (y2, x2) in itertools.permutations(positions, 2):
        dy, dx = y2-y1, x2-x1
        ay, ax = y2+dy, x2+dx
        if 0 <= ay < h and 0 <= ax < w:
            antinodes.add((ay, ax))
print('one', len(antinodes))

antinodes = set()
for freq, positions in antennas.items():
    for (y1, x1), (y2, x2) in itertools.permutations(positions, 2):
        dy, dx = y2-y1, x2-x1
        ay, ax = y2, x2
        while True:
            if 0 <= ay < h and 0 <= ax < w:
                antinodes.add((ay, ax))
                ay += dy
                ax += dx
            else:
                break
print('two', len(antinodes))
