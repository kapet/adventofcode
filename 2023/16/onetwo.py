data = [list(l.strip()) for l in open('2023/16/input.txt')]
width = len(data[0])
height = len(data)

def raytrace(starty, startx, stepy, stepx):
    beams = [(starty, startx, stepy, stepx)]
    completed = set()
    while beams:
        posy, posx, stepy, stepx = quad = beams.pop(0)
        if posy < 0 or posx < 0 or posy >= height or posx >= width:
            continue
        if quad in completed:
            continue
        completed.add(quad)
        match data[posy][posx]:
            case '/':
                stepy,stepx = -stepx,-stepy
            case '\\':
                stepy,stepx = stepx,stepy
            case '-':
                if stepy:
                    beams.append((posy, posx-1, 0, -1))
                    stepy,stepx = 0,1
            case '|':
                if stepx:
                    beams.append((posy-1,posx,-1,0))
                    stepy,stepx = 1,0
        beams.append((posy+stepy, posx+stepx, stepy, stepx))
    return len(set((y, x) for y, x, _, _ in completed))

print('one:', raytrace(0, 0, 0, 1))

two = 0
for x in range(width):
    two = max(two, raytrace(0, x, 1, 0))
    two = max(two, raytrace(height-1, x, -1, 0))
for y in range(height):
    two = max(two, raytrace(y, 0, 0, 1))
    two = max(two, raytrace(y, width-1, 0, -1))
print('two:', two)