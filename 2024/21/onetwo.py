import itertools
import functools

codes = [l.strip() for l in open('2024/21/input.txt')]

numpad = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    [None, '0', 'A'],
]

dirpad = [
    [None, '^', 'A'],
    ['<', 'v', '>'],
]

# I don't change the 'keypos' dicts later but want to use them for memoization
class hashabledict(dict):
    def __hash__(self):
        return hash(tuple(sorted(self.items())))

# convert key matrix into dict of key:(y,x)
def keypos(pad):
    pos = hashabledict()
    for y in range(len(pad)):
        for x in range(len(pad[0])):
            if (n := pad[y][x]) != None:
                pos[n] = (y, x)
    return pos
numpad_pos = keypos(numpad)
dirpad_pos = keypos(dirpad)

@functools.cache
def ysteps(my, ny):
    if ny > my:
        return ['v']*(ny-my)
    elif ny < my:
        return ['^']*(my-ny)
    else:
        return []

@functools.cache
def xsteps(mx, nx):
    if nx > mx:
        return ['>']*(nx-mx)
    elif nx < mx:
        return ['<']*(mx-nx)
    else:
        return []

# figure out if the path steps through the non-existing button, if yes path is not ok
@functools.cache
def legalpath(pos, start, steps):
    y, x = start
    for s in steps:
        if s == '>':
            x += 1
        elif s == '<':
            x -= 1
        elif s == 'v':
            y += 1
        elif s == '^':
            y -= 1
        else:
            raise Exception()
        if (y, x) not in pos.values():
            return False
    return True

# find all legal paths between button m and button n
@functools.cache
def allpath(pos, m, n):
    my, mx = pos[m]
    ny, nx = pos[n]
    steps = ysteps(my, ny) + xsteps(mx, nx)
    moves = []
    for perm in set(itertools.permutations(steps)):
        if legalpath(pos, (my, mx), perm):
            moves.append("".join(perm) + "A")
    return moves

# for the given code, find all paths for every button press
# e.g. 379A -> [['^A'], ['<^^<A', '^<^<A', '<^<^A', '<<^^A', '^<<^A', '^^<<A'], ['>>A'], ['vvvA']]
#               -> 3     -> 7                                                    -> 9     -> A
# there's only one shortest way to get to the 3, 9, and A, but several to go to the 7
@functools.cache
def allcomb(pos, code):
    s = 'A'
    combs = []
    for c in code:
        combs.append(allpath(pos, s, c))
        s = c
    return combs

# for the given directional code, find the length of the shortest path
@functools.cache
def find_shortest(code, depth):
    if depth == 0:
        return len(code)
    shortest = 0
    parts = allcomb(dirpad_pos, code)
    for part in parts:
        shortest += min(find_shortest(option, depth-1) for option in part)
    return shortest

one = 0
two = 0
for code in codes:
    parts = allcomb(numpad_pos, code)
    shortest_one = shortest_two = 0
    for part in parts:
        shortest_one += min(find_shortest(option, 2) for option in part)
        shortest_two += min(find_shortest(option, 25) for option in part)
    n = int(code[:3])
    one += shortest_one * n
    two += shortest_two * n

print('one', one)
print('two', two)


_ = '''
correct:
<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A

my, also correct, but not short:
v<<A>>^AvA^Av<<A>>^AAv<A<A>>^AAvAA<^A>Av<A>^AA<A>Av<A<A>>^AAAvA<^A>A
   <   A > A   <   AA  v <   AA >>  ^ A  v  AA ^ A  v <   AAA >  ^ A
       ^   A       ^^        <<       A     >>   A        vvv      A
           3                          7          9                 A

realization:
some 'shortest' paths are easier to type on dir pad
every 'substep' starts and ends at an 'A'
'''