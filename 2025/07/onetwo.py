import collections
import math

data = [l.strip() for l in open("2025/07/input.txt")]
h = len(data)
w = len(data[0])

one = 0
beams = collections.Counter({data[0].index('S'): 1})
for y in range(1, h):
    newbeams = collections.Counter()
    for x in beams.keys():
        if data[y][x] == "^":
            newbeams[x-1] += beams[x]
            newbeams[x+1] += beams[x]
            one += 1
        else:
            newbeams[x] += beams[x]
    beams = newbeams
two = int(math.fsum(beams.values()))
print("one", one)
print("two", two)