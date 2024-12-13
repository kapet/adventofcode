import dataclasses

@dataclasses.dataclass
class Config:
    ax: int
    ay: int
    bx: int
    by: int
    px: int
    py: int

configs = []
for entry in open('2024/13/input.txt').read().split('\n\n'):
    c = []
    for l in entry.split('\n'):
        l = l.strip().split(':')[1]
        c.extend([int(t.strip(' XY=')) for t in l.split(',')])
    configs.append(Config(*c))

_ = '''
n*ax + m*bx = px
n*ay + m*by = py

n*ax = px - m*bx
n*ay = py - m*by

n = (px - m*bx)/ax
n = (py - m*by)/ay

(px-m*bx) / ax = (py-m*by) / ay

ay*(px-m*bx) = ax*(py-m*by)

ay*px - ay*m*bx = ax*py - ax*m*by

ay*px - ax*py = ay*m*bx - ax*m*by = m*(ay*bx - ax*by)

m = (ay*px - ax*py) / (ay*bx - ax*by)
'''

one = 0
for c in configs:
    m, mr = divmod(c.ay*c.px - c.ax*c.py, c.ay*c.bx - c.ax*c.by)
    n, nr = divmod(c.px - m*c.bx, c.ax)

    if mr == 0 and nr == 0 and m <= 100 and n <= 100:
        one += n*3 + m*1
print('one', one)

two = 0
for c in configs:
    c.px += 10000000000000
    c.py += 10000000000000
    m, mr = divmod(c.ay*c.px - c.ax*c.py, c.ay*c.bx - c.ax*c.by)
    n, nr = divmod(c.px - m*c.bx, c.ax)
    if mr == 0 and nr == 0:
        two += n*3 + m*1
print('two', two)
