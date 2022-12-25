map_ = [list(line.strip()) for line in open('2022/24/input.txt')]

h = len(map_)
w = len(map_[0])

def findPathLength(blizzards, start, goal):
    positions = set()
    positions.add(start)
    steps = 0
    found = False
    while not found:
        new_blizzards = {}
        for (y_old, x_old), directions in blizzards.items():
            for direction in directions:
                x, y = x_old, y_old
                if direction == '>':
                    x += 1
                    if x == w-1:
                        x = 1
                elif direction == '<':
                    x -= 1
                    if x == 0:
                        x = w-2
                elif direction == 'v':
                    y += 1
                    if y == h-1:
                        y = 1
                elif direction == '^':
                    y -= 1
                    if y == 0:
                        y = h-2
                else:
                    raise Exception()
                new_blizzards.setdefault((y, x), []).append(direction)

        new_positions = set()
        for y, x in positions:
            wait = (y, x)
            if wait not in new_blizzards:
                new_positions.add(wait)
            right = (y, x+1)
            if y > 0 and y < h-1 and right[1] < (w-1) and right not in new_blizzards:
                new_positions.add(right)
            left = (y, x-1)
            if y > 0 and y < h-1 and left[1] > 0 and left not in new_blizzards:
                new_positions.add(left)
            down = (y+1, x)
            if down[0] < (h-1) and down not in new_blizzards:
                new_positions.add(down)
            up = (y-1, x)
            if up[0] > 0 and up not in new_blizzards:
                new_positions.add(up)
            if down == goal or up == goal:
                found = True

        blizzards = new_blizzards
        positions = new_positions
        steps += 1

        if 0:
            print('after', steps, len(positions))
            print('#'*w)
            for y in range(1, h-1):
                row = ['#']
                for x in range(1, w-1):
                    t = blizzards.get((y,x), [])
                    if not t:
                        if (y,x) in positions:
                            row.append('.')
                        else:
                            row.append(' ')
                    else:
                        assert (y,x) not in positions
                        if len(t) == 1:
                            row.append(t[0])
                        else:
                            row.append(str(len(t)))
                row.append('#')
                print(''.join(row))
            print('#'*w)

    return blizzards, steps


start = (0, 1)
goal = (h-1, w-2)

blizzards = {}
for y in range(1, h-1):
    for x in range(1, w-1):
        if map_[y][x] != '.':
            blizzards[(y, x)] = [map_[y][x]]

blizzards, one = findPathLength(blizzards, start, goal)
print('one:', one)
blizzards, two = findPathLength(blizzards, goal, start)
blizzards, three = findPathLength(blizzards, start, goal)
print('two:', one+two+three)
