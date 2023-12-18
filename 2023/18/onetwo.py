plan = [(l[0], int(l[1]), l[2][1:-1]) for l in (line.split() for line in open('2023/18/test.txt'))]

coords = []
posy = posx = 0
miny = minx = 0
maxx = maxy = 0
for direction, distance, _ in plan:
    oldy, oldx = posy, posx
    match direction:
        case 'R':
            posx += distance
        case 'D':
            posy += distance
        case 'L':
            posx -= distance
        case 'U':
            posy -= distance
    miny = min(miny, posy)
    minx = min(minx, posx)
    maxy = max(maxy, posy)
    maxx = max(maxx, posx)
    coords.append(((oldy, oldx), (posy, posx)))
coords = [((c[0][0]-miny,c[0][1]-minx),(c[1][0]-miny,c[1][1]-minx)) for c in coords]
width = maxx-minx+1
height = maxy-miny+1

def sign(x):
    return (x > 0) - (x < 0)

field = [['.']*width for _ in range(height)]
for (sy,sx), (ey,ex) in coords:
    iy = sign(ey-sy)
    ix = sign(ex-sx)
    while (sy,sx) != (ey, ex):
        sy += iy
        sx += ix
        field[sy][sx] = '#'

posy = 1
posx = field[posy].index('#') + 1
heap = [(posy, posx)]
while heap:
    posy, posx = heap.pop()
    if field[posy][posx] == '#':
        continue
    field[posy][posx] = '#'
    for y,x in ((posy-1,posx),(posy+1,posx),(posy,posx-1),(posy,posx+1)):
        if field[y][x] == '.':
            heap.append((y,x))

print('one:', sum(l.count('#') for l in field))

newplan = []
for _, _, color in plan:
    distance = int(color[1:6], 16)
    direction = 'RDLU'[int(color[6])]
    newplan.append((direction, distance))
print(newplan)
