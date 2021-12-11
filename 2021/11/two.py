data = []
for line in open('2021/11/input.txt'):
    data.append([int(i) for i in line.strip()])

height = len(data)
width = len(data[0])

flashed = [[False]*width for _ in range(height)]

def print_matrix():
    for y in range(height):
        line = []
        for x in range(width):
            c = str(data[y][x])
            if flashed[y][x]:
                # give it a yellow background if it flashed
                c = '\033[103m' + c + '\033[0m'
            line.append(c)
        print(''.join(line))
    print('-'*width)

def neighbors(x, y):
    l = x > 0
    r = x < width-1
    t = y > 0
    b = y < height-1
    if t:
        if l:
            yield (x-1, y-1)
        yield (x, y-1)
        if r:
            yield (x+1, y-1)
    if l:
        yield (x-1, y)
    if r:
        yield (x+1, y)
    if b:
        if l:
            yield (x-1, y+1)
        yield (x, y+1)
        if r:
            yield (x+1, y+1)

print('before any steps')
print_matrix()

for step in range(1,10001):
    flashes = 0
    flashed = [[False]*width for _ in range(height)]
    stack = []
    for y in range(height):
        for x in range(width):
            data[y][x] += 1
            if data[y][x] > 9:
                stack.append((x, y))
                flashed[y][x] = True
    for x, y in stack:
        data[y][x] = 0
        flashes += 1
        for nx, ny in neighbors(x, y):
            if not flashed[ny][nx]:
                data[ny][nx] += 1
                if data[ny][nx] > 9:
                    stack.append((nx, ny))
                    flashed[ny][nx] = True

    print('after step {} and {} flashes'.format(step, flashes))
    print_matrix()
    if flashes == width*height:
        break