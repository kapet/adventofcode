data = [list(l.strip()) for l in open('2024/04/input.txt')]
w = len(data[0])
h = len(data)

LINEAR_DIRECTIONS = [
    (0, 1),  # e
    (1, 1),  # se
    (1, 0),  # s
    (1, -1), # sw
    (0, -1), # w
    (-1, -1), # nw
    (-1, 0), # n
    (-1, 1), # ne
 ]

def linear_stencil(y, x, dy, dx):
    return [(y,x), (y+dy,x+dx), (y+2*dy,x+2*dx), (y+3*dy,x+3*dx)]

def all_linear_stencils(y, x):
    return [linear_stencil(y, x, dy, dx) for dy, dx in LINEAR_DIRECTIONS]

def x_stencils(y, x):
    return [
        ((y-1, x-1), (y+1, x-1), (y, x), (y-1, x+1), (y+1, x+1)), # e
        ((y-1, x+1), (y+1, x+1), (y, x), (y-1, x-1), (y+1, x-1)), # w
        ((y-1, x-1), (y-1, x+1), (y, x), (y+1, x-1), (y+1, x+1)), # s
        ((y+1, x-1), (y+1, x+1), (y, x), (y-1, x-1), (y-1, x+1)), # n
    ]

def good_stencils(stencils):
    return [stencil for stencil in stencils if not any(x<0 or x>=w or y<0 or y>=h for x, y in stencil)]

def get(stencil):
    return ''.join(data[y][x] for y, x in stencil)

one = two = 0
for sy in range(h):
    for sx in range(w):
        stencils = all_linear_stencils(sy, sx)
        stencils = good_stencils(stencils)
        one += sum(get(stencil) == 'XMAS' for stencil in stencils)

        stencils = x_stencils(sy, sx)
        stencils = good_stencils(stencils)
        two += sum(get(stencil) == 'MMASS' for stencil in stencils)

print('one', one)
print('two', two)
