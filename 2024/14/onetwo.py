import dataclasses
import re

@dataclasses.dataclass
class Robot:
    px: int
    py: int
    vx: int
    vy: int

r = re.compile(r'p=(\d+),(\d+) v=(.*),(.*)$')
data = [Robot(*map(int, r.match(l).groups())) for l in open('2024/14/input.txt')]

if data[0].px == 0:
    w = 11
    h = 7
else:
    w = 101
    h = 103

q1 = q2 = q3 = q4 = 0
w2 = w//2
h2 = h//2
for r in data:
    px = (r.px + r.vx*100) % w
    py = (r.py + r.vy*100) % h
    if px < w2 and py < h2:
        q1 += 1
    elif px > w2 and py < h2:
        q2 += 1
    elif px < w2 and py > h2:
        q3 += 1
    elif px > w2 and py > h2:
        q4 += 1
    else:
        # on the centerline
        pass
print('one', q1*q2*q3*q4)

def l2s(l):
    return ''.join(map(str, l)).replace('0', ' ')

if 0:
    # try printing every result and look for anything odd
    output = open('2024/14/out1000.txt', 'w')
    for i in range(1000):
        mymap = [[0]*w for _ in range(h)]
        for r in data:
            r.px = (r.px + r.vx) % w
            r.py = (r.py + r.vy) % h
            mymap[r.py][r.px] += 1
        output.write(f'\n\n{i+1}\n')
        output.writelines(l2s(l)+'\n' for l in mymap)

_ = '''
there are two repeating 'structures' in the data, one at 75 and then every 103 steps,
the other one at 27 and then every 101 steps

assumption: they need to apply at the same time

27+101*i = 75+103*i
101*i-103*i = 75-27
-2*i = 48
i = -24

that means at iteration 27+101*-24 = -2397

assumption: the overall cycle repeats every w*h = 101*103 = 10403 iterations

so then lets look at iteration 10403-2397 = 8006
'''

output = open('2024/14/two.txt', 'w')
mymap = [[0]*w for _ in range(h)]
for r in data:
    px = (r.px + r.vx*8006) % w
    py = (r.py + r.vy*8006) % h
    mymap[py][px] += 1
output.writelines(l2s(l)+'\n' for l in mymap)
