field = [list(line.strip()) for line in open('2023/10/input.txt')]
width = len(field[0])
height = len(field)

# Find the start position
for starty, line in enumerate(field):
    if 'S' in line:
        startx = line.index('S')
        break

# Detect the start symbol from its surroundings and fill it in
start_symbol = set('|-7FLJ')
if starty > 0 and field[starty-1][startx] in '|7F':
    start_symbol &= set('|LJ')
if starty < height-1 and field[starty+1][startx] in '|LJ':
    start_symbol &= set('|7F')
if startx > 0 and field[starty][startx-1] in '-LF':
    start_symbol &= set('-J7')
if startx < width-1 and field[starty][startx+1] in '-J7':
    start_symbol &= set('-LF')
assert len(start_symbol) == 1
field[starty][startx] = start_symbol.pop()

# Detect the loop and calculate distances
next = [(0, starty, startx)]
distances = [['.']*width for _ in range(height)]
one = 0
while next:
    dist, posy, posx = next.pop(0)
    if distances[posy][posx] == '.':
        distances[posy][posx] = dist
        one = max(one, dist)
        match field[posy][posx]:
            case '|':
                next.append((dist+1, posy-1, posx))
                next.append((dist+1, posy+1, posx))
            case '-':
                next.append((dist+1, posy, posx-1))
                next.append((dist+1, posy, posx+1))
            case 'L':
                next.append((dist+1, posy-1, posx))
                next.append((dist+1, posy, posx+1))
            case 'J':
                next.append((dist+1, posy-1, posx))
                next.append((dist+1, posy, posx-1))
            case '7':
                next.append((dist+1, posy+1, posx))
                next.append((dist+1, posy, posx-1))
            case 'F':
                next.append((dist+1, posy+1, posx))
                next.append((dist+1, posy, posx+1))
print('one:', one)

# Create a larger version of the board in which all chars are tripled in size:
#       .|.         ...
#  L -> .L-    - -> ---
#       ...         ...
# This creates space ('.') between all pipes to allow the flood fill through.
field3 = []
for y in range(height):
    line3 = []
    for x in range(width):
        this = ['.']*9
        if distances[y][x] == '.':
            # mark all center fields not part of the loop
            this[4] = 'I'
        else:
            this[4] = c = field[y][x]
            if c in '|LJ': # north
                this[1] = '|'
            if c in '|7F': # south
                this[7] = '|'
            if c in '-J7': # west
                this[3] = '-'
            if c in '-LF': # east
                this[5] = '-'
        line3.append(this)
    for i in range(3):
        field3.append(list(s for t in line3 for s in t[i*3:i*3+3]))
height3 = len(field3)
width3 = len(field3[0])

# Flood fill all reachable fields from the outside in.
next = set([(0,0)])
while next:
    posy, posx = next.pop()
    if field3[posy][posx] in '.I':
        field3[posy][posx] = 'O'
        if posy > 0:
            next.add((posy-1, posx))
        if posy < height3-1:
            next.add((posy+1, posx))
        if posx > 0:
            next.add((posy, posx-1))
        if posx < width3-1:
            next.add((posy, posx+1))

# All fields still marked 'I' were not reachable by the flood fill and
# therefore must be internal to the loop.
print('two:', sum(l.count('I') for l in field3))
