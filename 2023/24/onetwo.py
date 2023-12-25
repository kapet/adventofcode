hailstones = []
for line in open('2023/24/input.txt'):
    line = list(map(int, line.replace('@','').replace(',', '').split()))
    hailstones.append((line[0:3], line[3:]))


_ = '''
math notes, based on https://stackoverflow.com/questions/73079419/intersection-of-two-vector

one line is:
    points = [x, y]*s + [a, b]
with [x, y] being the vector, [a, b] is the base, and s runs along the line

setting two lines equal to look for the crossover point:
    [x_1, y_1]*s_1 + [a_1, b_1] = [x_2, y_2]*s_2 + [a_2, b_2]

rearranged into "v*x=b" matrix form:
    |x_1, -x_2| * |s_1| = |a_2 - a_1|
    |y_1, -y_2|   |s_2|   |b_2 - b_1|

side note, inverse of a matrix:
    |a, b|^-1 = 1/(ad - bc) * | d, -b|
    |c, d|                    |-c,  a|

rearranged into "x=v^-1*b" form:
    |s_1| = 1/(x_2*y_1 - x_1*y_2) * |-y_2, x_2| * |a_2 - a_1|
    |s_2|                           |-y_1, x_1|   |b_2 - b_1|

splitting the denominator out:
    denom = x_2*y_1 - x_1*y_2

solving for s_1 and s_2:
    s_1 = 1/denom * ((b_2-b_1)*x_2 - (a_2-a_1)*y_2)
    s_2 = 1/denom * ((b_2-b_1)*x_1 - (a_2-a_1)*y_1)
'''

test_min = 200000000000000
test_max = 400000000000000

one = 0
for i, (base1, vector1) in enumerate(hailstones[:-1]):
    for base2, vector2 in hailstones[i+1:]:
        denom = vector2[0]*vector1[1] - vector1[0]*vector2[1]
        if denom:
            denom = 1/denom
            xdiff = base2[0]-base1[0]
            ydiff = base2[1]-base1[1]
            s1 = denom * (ydiff*vector2[0] - xdiff*vector2[1])
            s2 = denom * (ydiff*vector1[0] - xdiff*vector1[1])
            if s1 < 0 and s2 < 0:
                print(base1, base2, 'crossed in the past for both')
            elif s1 < 0:
                print(base1, base2, 'crossed in the past for A')
            elif s2 < 0:
                print(base1, base2, 'crossed in the past for B')
            else:
                posx = base1[0] + vector1[0] * s1
                posy = base1[1] + vector1[1] * s1
                if test_min <= posx <= test_max and test_min <= posy <= test_max:
                    print(base1, base2, 'within test area')
                    one += 1
                else:
                    print(base1, base2, 'outside test area')
        else:
            print(base1, base2, 'do not intersect')
print('one:', one)
