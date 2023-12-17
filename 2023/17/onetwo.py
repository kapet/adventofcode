import heapq

blocks = [list(int(l) for l in line.strip()) for line in open('2023/17/input.txt')]
width = len(blocks[0])
height = len(blocks)

RIGHT = 1
DOWN = 2
LEFT = 3
UP = 4

def drive_crucible(min_straight, max_straight):
    heap = [(0, 1, 1,0, DOWN), (0, 1, 0,1, RIGHT)]
    visited = [[{} for _ in range(width)] for _ in range(height)]

    while heap:
        heatloss, nstraight, posy,posx, direction = heapq.heappop(heap)
        heatloss += blocks[posy][posx]

        # check current field and mark as visited
        v = visited[posy][posx]
        key = (direction, nstraight)
        if key in v and heatloss >= v[key]:
            continue
        v[key] = heatloss

        # figure out possible directions
        d = [None, True, True, True, True]
        if nstraight < min_straight:
            d = [None, False, False, False, False]
            d[direction] = True
        elif nstraight+1 > max_straight:
            d[direction] = False
        d[(0,3,4,1,2)[direction]] = False

        if d[RIGHT] and posx+1<width:
            heapq.heappush(heap, (heatloss, direction==RIGHT and nstraight+1 or 1, posy,posx+1, RIGHT))
        if d[DOWN] and posy+1<height:
            heapq.heappush(heap, (heatloss, direction==DOWN and nstraight+1 or 1, posy+1,posx, DOWN))
        if d[LEFT] and posx>0:
            heapq.heappush(heap, (heatloss, direction==LEFT and nstraight+1 or 1, posy,posx-1, LEFT))
        if d[UP] and posy>0:
            heapq.heappush(heap, (heatloss, direction==UP and nstraight+1 or 1, posy-1,posx, UP))

    return min(visited[-1][-1].values())

print('one:', drive_crucible(1, 3))
print('two:', drive_crucible(4, 10))
