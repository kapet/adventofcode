data = [line.split() for line in open('2023/18/input.txt')]

plan_one = []
plan_two = []
for line in data:
    plan_one.append((line[0], int(line[1])))

    color = line[2]
    distance = int(color[2:7], 16)
    direction = 'RDLU'[int(color[7])]
    plan_two.append((direction, distance))

def to_coordinates(plan):
    coords = []
    posy = posx = 0
    for direction, distance in plan:
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
        coords.append(((oldy, oldx), (posy, posx)))
    return coords

def calc_pixel_area(coords):
    # The coordinates represent a polygon.
    # Use Shoelace formula to calculate surface area.
    # This gives wrong result because of fence post issue with the pixels.
    # To correct: Think of polygon outline being in the center of the pixels.
    # Now every step on a line misses 1/2 pixel, so that means add half of the
    # total outline of the polygon. And every corner either misses or gains
    # 1/4 pixel. But corners balance each other out, except for four corners
    # that each miss 1/4 pixel -> add one extra pixel.  
    result = 0
    outline = 0
    for (sy,sx),(ey,ex) in coords:
        outline += abs(ey-sy)+abs(ex-sx)
        result += (sy+ey)*(sx-ex)
    return abs(result//2) + outline//2 + 1

coords_one = to_coordinates(plan_one)
print('one:', calc_pixel_area(coords_one))

coords_two = to_coordinates(plan_two)
print('two:', calc_pixel_area(coords_two))
