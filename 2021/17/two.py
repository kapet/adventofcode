import math

testdata = (20, 30, -10, -5)
inputdata = (138, 184, -125, -71)

xmin, xmax, ymin, ymax = inputdata
print('target area: x={}..{}, y={}..{}'.format(xmin, xmax, ymin, ymax))

# xvel options are limited: if starting velocity is too small we never get there,
# and if it's too high then the first step will already be beyond the target.

# First calculate the absolute minimum possible velocity, this is based on
# Gauss summation method filled into pq-formula.
xvelmin = math.floor(-0.5 + math.sqrt(0.25 + 2*xmin))

# Absolute maximum for xvel is xmax itself, any bigger and we'd never hit target.
xvelmax = xmax

# yvel can either be positive ('balistic' arc) or negative ('direct').

# 'balistic' arcs always hit 0 on the way down, and with the same velocity as originally started,
# just in the other direction and one more negative. (E.g. +3 -> -4)
# The next step after that must not go beyond the target.
yvelmax = abs(ymin)

# 'direct' arcs use yvel for the first step, if that goes past the target then
# again no larger (more negative) yvel will ever hit.
yvelmin = ymin

print('xvel={}..{} yvel={}..{}'.format(xvelmin, xvelmax, yvelmin, yvelmax))

def run(xvel, yvel):
    x, y = 0, 0
    while True:
        x += xvel
        y += yvel
        if xvel > 0:
            xvel -= 1  # (xvel > 0) - (xvel < 0)  unneccessary, never <0
        yvel -= 1

        if x >= xmin and x <= xmax and y >=ymin and y <= ymax:
            return True
        if x > xmax or (xvel == 0 and x < xmin) or y < ymin:
            return False

hitters = []
for xv in range(xvelmin, xvelmax+1):
    for yv in range(yvelmin, yvelmax+1):
        if run(xv, yv):
            hitters.append((xv, yv))
print(hitters)
print(len(hitters))