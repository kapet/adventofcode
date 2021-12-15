import time
import collections

_cavern = [list(map(int, l.strip())) for l in open('2021/15/input.txt')]
_height = len(_cavern)
_width = len(_cavern[0])

def cavern(x, y):
    xd, xr = divmod(x, _width)
    yd, yr = divmod(y, _height)
    return ((_cavern[yr][xr]-1 + xd + yd) % 9) + 1
height = _height * 5
width = _width * 5

def neighbours(x, y):
    if y > 0:
        yield (x, y-1)
    if x > 0:
        yield (x-1, y)
    if x < width-1:
        yield (x+1, y)
    if y < height-1:
        yield (x, y+1)

shortest_successor = [[None]*width for _ in range(height)]
shortest_successor[0][0] = (0, 0, 0)

# there will often be a new shortest path found multiple times for the same position,
# which is already in the todo list - slowing things down a lot. No point keeping all
# those wrong intermediate stages, it's enough to just remember the shortest one 
todo = collections.OrderedDict()
todo[(0, 0)] = 0
t = time.time()
steps = 0
while todo:
    pos, cost = todo.popitem(last=False)
    x, y = pos
    for nx, ny in neighbours(x, y):
        ncost = cost+cavern(nx, ny)
        n = shortest_successor[ny][nx]
        if n is None or ncost < n[2]:
            shortest_successor[ny][nx] = (x, y, ncost)
            todo[(nx, ny)] = ncost

    steps += 1
    tn = time.time()
    if tn-t > 1:
        t = tn
        print(steps, len(todo))

print(shortest_successor[-1][-1])