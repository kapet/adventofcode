cavern = [list(map(int, l.strip())) for l in open('2021/15/input.txt')]

height = len(cavern)
width = len(cavern[0])

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
todo = [(0, 0, 0)]
while todo:
    x, y, cost = todo.pop(0)
    for nx, ny in neighbours(x, y):
        ncost = cost+cavern[ny][nx]
        n = shortest_successor[ny][nx]
        if n is None or ncost < n[2]:
            shortest_successor[ny][nx] = (x, y, ncost)
            todo.append((nx, ny, ncost))

    if len(todo) < 3:
        print('----------------------')
        for y in range(height):
            out = []
            for x in range(width):
                n = shortest_successor[y][x]
                if n is None:
                    out.append('-')
                else:
                    nx, ny, _ = n
                    if nx < x:
                        out.append('<')
                    elif nx > x:
                        out.append('>')
                    elif ny < y:
                        out.append('^')
                    elif ny > y:
                        out.append('v')
                    else:
                        out.append('0')
            print(''.join(out))

print(shortest_successor[-1][-1])