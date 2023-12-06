import math

with open('2023/06/input.txt') as infile:
    times = infile.readline().split()[1:]
    distances = infile.readline().split()[1:]

# Distance traveled in a race of length TIME after charging for X milliseconds:
#   distance = (time-x) * x
#
# This can be rearranged into a quadratic equation:
#   -1*x*x + time*x - distance = 0
#
# We actually know the TIME for a race and the DISTANCE to beat,
# so we can calculate the actual zeros! The boat will beat the distance with a
# charging time "between" the zeros. Formulas for finding the zeros:
#   D = b*b - 4*a*c
#   x = (-b +- sqrt(D)) / 2*a
# Using: a=-1  b=time  c=-distance
#   Droot = sqrt(time*time - 4*distance)
#   z1 = (-time + Droot) / -2
#   z2 = (-time - Droot) / -2
#
# It's not enough to achieve the exact given DISTANCE, we need to beat it.
# So increment DISTANCE by one before putting it in the formula.
#
# We can only charge full milliseconds, so need to round up the lower limit
# and round down the upper limit to the nearest integer.

def limits(time_, distance):
    Droot = math.sqrt(time_*time_ - 4*distance)
    return (-time_ + Droot) / -2, (-time_ - Droot) / -2

def ways_to_beat(time_, distance):
    z1, z2 = limits(time_, distance+1)
    return math.floor(z2)-math.ceil(z1)+1

one = 1
for time_, distance in zip(map(int, times), map(int, distances)):
    one *= ways_to_beat(time_, distance)
print("one:", one)

print("two:", ways_to_beat(int(''.join(times)), int(''.join(distances))))
