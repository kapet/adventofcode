import dataclasses
import heapq

mymap = [list(l.strip()) for l in open('2024/16/input.txt')]
w = len(mymap[0])
h = len(mymap)
startx, starty = 1, h-2
endx, endy = w-2, 1

@dataclasses.dataclass(order=True)
class Element:
    x: int=dataclasses.field(compare=False)
    y: int=dataclasses.field(compare=False)
    direction: str=dataclasses.field(compare=False)
    cost: int

ALL_DIRECTIONS = [(-1, 0, '^'), (0, -1, '<'), (1, 0, 'v'), (0, 1, '>')] * 2
DIRECTIONS = {ALL_DIRECTIONS[i+1][2]:ALL_DIRECTIONS[i:i+3] for i in range(4)}

# (y, x) -> direction -> min cost
visited = {}

stack = [Element(startx, starty, '>', 0)]
finished = []
min_finished = None
while stack:
    e = heapq.heappop(stack)

    v = visited.setdefault((e.y, e.x), {})
    if e.direction in v and v[e.direction] <= e.cost:
        continue
    v[e.direction] = e.cost

    if (e.x, e.y) == (endx, endy):
        if not finished or e.cost < min_finished:
            finished = [e]
            min_finished = e.cost
        elif e.cost == min_finished:
            finished.append(e)
        continue

    for dy, dx, dd in DIRECTIONS[e.direction]:
        nc = dd==e.direction and e.cost+1 or e.cost+1000+1
        ne = Element(e.x+dx, e.y+dy, dd, nc)
        if mymap[ne.y][ne.x] == '#':
            continue
        heapq.heappush(stack, ne)

print('one', min_finished)

assert len(finished) == 1

REVERSES = {ALL_DIRECTIONS[i+1][2]:[(ALL_DIRECTIONS[i+1][0], ALL_DIRECTIONS[i+1][1], ALL_DIRECTIONS[i+j][2]) for j in range(3)] for i in range(4)}

marked = {}
stack = finished
while stack:
    e = stack.pop()
    marked[(e.x, e.y)] = e.direction
    if e.y == starty and e.x == startx:
        continue

    for dy, dx, dd in REVERSES[e.direction]:
        if dd == e.direction:
            nc = e.cost - 1
        else:
            nc = e.cost - 1000 - 1
        ne = Element(e.x-dx, e.y-dy, dd, nc)
        v = visited[(ne.y, ne.x)]
        if ne.direction in v and v[ne.direction] == ne.cost:
            stack.append(ne)

print('two', len(marked))