h = v = aim = 0
for l in open('2021/02/input.txt'):
    cmd, dist = l.split()
    dist = int(dist)
    if cmd == 'forward':
        h += dist
        v += aim * dist
    elif cmd == 'up':
        aim -= dist
    elif cmd == 'down':
        aim += dist
    else:
        raise Exception('unknown command: ' + cmd)
print(h, v, h*v)