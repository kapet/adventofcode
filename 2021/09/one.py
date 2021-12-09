heightmap = []
for line in open('2021/09/input.txt'):
    line = list(line.strip())
    line = list(map(int, line))
    heightmap.append(line)

minx = miny = 0
maxx = len(heightmap[0])-1
maxy = len(heightmap)-1

low_sum = 0
for y in range(maxy+1):
    for x in range(maxx+1):
        this = heightmap[y][x]
        if y > miny and this >= heightmap[y-1][x]:
            pass
        elif y < maxy and this >= heightmap[y+1][x]:
            pass
        elif x > minx and this >= heightmap[y][x-1]:
            pass
        elif x < maxx and this >= heightmap[y][x+1]:
            pass
        else:
            # it's a low point
            low_sum += 1 + this

print(low_sum)