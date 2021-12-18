testdata = (20, 30, -10, -5)
inputdata = (138, 184, -125, -71)

xmin, xmax, ymin, ymax = inputdata
print('target area: x={}..{}, y={}..{}'.format(xmin, xmax, ymin, ymax))

def run(xvel, yvel):
    _xvel, _yvel = xvel, yvel
    x, y = 0, 0
    max_h = 0
    while True:
        x += xvel
        y += yvel
        if y > max_h:
            max_h = y
        if xvel > 0:
            xvel -= 1  # (xvel > 0) - (xvel < 0)  unneccessary, never <0
        yvel -= 1
        #print('  after step: x={}, y={}, xvel={}, yvel={}'.format(x, y, xvel, yvel))

        if x >= xmin and x <= xmax and y >=ymin and y <= ymax:
            print('success ({}, {}) -> {}'.format(_xvel, _yvel, max_h))
            return max_h
        if x > xmax or (xvel == 0 and x < xmin) or y < ymin:
            return -1

# heuristic: x velocity is trivial when shooting on a 'balistic' trajectory,
# we can forecast which values makes sense at all
x = 0
xinc = 1
xvelmin, xvelmax = 0, 0
for i in range(1, xmax):
    x += xinc
    xinc += 1
    if x >= xmin and xvelmin == 0:
        xvelmin = i
    elif x > xmax:
        xvelmax = i-1
        break
print('x velocity can only be within {}..{} to reach the target'.format(xvelmin, xvelmax))

max_height = 0
for xv in range(xvelmin, xvelmax+1):
    for yv in range(abs(ymin)*2):
        t = run(xv, yv)
        if t > max_height:
            max_height = t
print(max_height)