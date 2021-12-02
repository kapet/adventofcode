h = v = 0
for l in open('2021/02/input.txt'):
    cmd, dist = l.split()
    dist = int(dist)
    if cmd == 'forward':
        h += dist
    elif cmd == 'up':
        v -= dist
    elif cmd == 'down':
        v += dist
    else:
        raise Exception('unknown command: ' + cmd)
print(h, v, h*v)
