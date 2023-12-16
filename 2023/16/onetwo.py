data = [list(l.strip()) for l in open('2023/16/input.txt')]
width = len(data[0])
height = len(data)

lookup_reverse = [0, 2, 1, 0, 8, 0, 0, 0, 4]
lookup_nwse = [0, 4, 8, 0, 1, 0, 0, 0, 2]   # \
lookup_nesw = [0, 8, 4, 0, 2, 0, 0, 0, 1]   # /

def raytrace(starty, startx, stepy, stepx):
    beams = [(starty, startx, stepy, stepx)]
    marked = 0
    completed = [0]*width*height
    while beams:
        posy, posx, stepy, stepx = beams.pop()
        key = stepy and (stepy<0 and 1 or 2) or (stepx<0 and 4 or 8)
        while posy >= 0 and posx >= 0 and posy < height and posx < width:
            comp = completed[posy*width + posx]
            if not comp:
                marked += 1
                comp = key
            elif comp & key:
                break
            else:
                comp |= key
            match data[posy][posx]:
                case '.':
                    comp |= lookup_reverse[key]
                case '/':
                    stepy,stepx = -stepx,-stepy
                    key = lookup_nesw[key]
                    comp |= lookup_reverse[key]
                case '\\':
                    stepy,stepx = stepx,stepy
                    key = lookup_nwse[key]
                    comp |= lookup_reverse[key]
                case '-':
                    comp |= lookup_reverse[key]
                    if stepy:
                        beams.append((posy, posx-1, 0, -1))
                        stepy,stepx = 0,1
                        key = 8
                case '|':
                    comp |= lookup_reverse[key]
                    if stepx:
                        beams.append((posy-1,posx,-1,0))
                        stepy,stepx = 1,0
                        key = 2
            completed[posy*width+posx] = comp
            posy += stepy
            posx += stepx
    return marked

print('one:', raytrace(0, 0, 0, 1))

two = 0
for x in range(width):
    two = max(two, raytrace(0, x, 1, 0))
    two = max(two, raytrace(height-1, x, -1, 0))
for y in range(height):
    two = max(two, raytrace(y, 0, 0, 1))
    two = max(two, raytrace(y, width-1, 0, -1))
print('two:', two)
