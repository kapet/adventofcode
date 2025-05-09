data = [(l[0], int(l[1:])) for l in open('2020/12/input.txt')]

fy, fx = 0, 1
y = x = 0
for cmd, n in data:
    match cmd:
        case 'N':
            y -= n
        case 'S':
            y += n
        case 'E':
            x += n
        case 'W':
            x -= n
        case 'L':
            assert n % 90 == 0 and n > 0
            while n > 0:
                fy, fx = -fx, fy
                n -= 90
        case 'R':
            assert n % 90 == 0 and n > 0
            while n > 0:
                fy, fx = fx, -fy
                n -= 90
        case 'F':
            y += fy * n
            x += fx * n
print('one', abs(y)+abs(x))

wy, wx = -1, 10
y = x = 0
for cmd, n in data:
    match cmd:
        case 'N':
            wy -= n
        case 'S':
            wy += n
        case 'E':
            wx += n
        case 'W':
            wx -= n
        case 'L':
            while n > 0:
                wy, wx = -wx, wy
                n -= 90
        case 'R':
            while n > 0:
                wy, wx = wx, -wy
                n -= 90
        case 'F':
            y += wy * n
            x += wx * n
print('two', abs(y)+abs(x))
