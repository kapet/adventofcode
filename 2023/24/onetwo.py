import numpy as np
import sympy

hailstones = []
for line in open('2023/24/input.txt'):
    line = list(map(int, line.replace('@','').replace(',', '').split()))
    hailstones.append((np.array(line[0:3]), np.array(line[3:])))

_ = '''
math notes, based on https://stackoverflow.com/questions/73079419/intersection-of-two-vector

one line is:
    points = m*t + b
with m=[x, y] being the vector, b=[x, y] is the base position, and t is the time

setting two lines equal to look for the crossover point:
    m1*t1 + b1 = m2*t1 + b2

rearranged into "Ax=b" matrix form:
    |m1.x, -m2.x| * |t1| = |b2.x - b1.x|
    |m1.y, -m2.y|   |t2|   |b2,y - b1.y|

this can be solved for [t1, t2] with numpy.linalg.solve
'''

if len(hailstones) == 5:
    test_min, test_max = 7, 27
else:
    test_min, test_max = 200000000000000,400000000000000

one = 0
for i, (b1, m1) in enumerate(hailstones[:-1]):
    b1 = np.delete(b1, 2)
    m1 = np.delete(m1, 2)
    for b2, m2 in hailstones[i+1:]:
        b2 = np.delete(b2, 2)
        m2 = np.delete(m2, 2)
        b = b2 - b1
        A = np.column_stack((m1, -m2))
        try:
            t1,t2 = np.linalg.solve(A,b)
            if t1 < 0 and t2 < 0:
                # crossed in the past for both
                pass
            elif t1 < 0:
                # crossed in the past for A
                pass
            elif t2 < 0:
                # crossed in the past for B
                pass
            else:
                x, y = b1 + m1 * t1
                if test_min <= x <= test_max and test_min <= y <= test_max:
                    # within test area
                    one += 1
                else:
                    # outside test area
                    pass
        except np.linalg.LinAlgError:
            # lines do not intersect
            pass
print('one:', one)

_ = '''
more math notes

the input data must be crafted so that all hailstone lines eventually
intersect with the same line-to-find, but at different times

this creates an equation system like this, for 0 being the one to find:
    m1*t1 + b1 = m0*t1 + b0
    m2*t2 + b2 = m0*t2 + b0
    m3*t3 + b3 = m0*t3 + b0
    etc. for all hailstones

here I tried reforming these equations into a solvable system, but the
intermediate terms become unbearable large - too much work

Reading up on reddit on how others solved this is full of math that
I'm not fluent in and don't want to pick up now. So let's find a way
to let the computer solve it. First try with just dumping everything
in Wolfram Alpha failed b/o input length limits.

After some more digging decided to use sympy. *shrug*
'''

bx = sympy.symbols('bx by bz')
mx = sympy.symbols('mx my mz')
tx = sympy.symbols('t1 t2 t3')
equations = []
for i, (b, m) in enumerate(hailstones[:3]):
    for j in range(3): # x/y/z coordinates
        equations.append(sympy.Eq(m[j]*tx[i]+b[j], mx[j]*tx[i]+bx[j]))
results = sympy.solve(equations)[0]
print('two:', sum(results[t] for t in bx))
