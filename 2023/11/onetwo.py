image_raw = [list(line.strip()) for line in open('2023/11/input.txt')]

# expand vertically for every empty line
image_ver = []
for line in image_raw:
    image_ver.append(line)
    if '#' not in line:
        image_ver.append(line)

# rotate by 90 degree and then expand 'horizontally'
# this is easier that working by columns
image_ver = list(zip(*reversed(image_ver)))
image_hor = []
for line in image_ver:
    image_hor.append(line)
    if '#' not in line:
        image_hor.append(line)
image = list(reversed(list(zip(*image_hor))))
width = len(image[0])
height = len(image)

# find all galaxies
galaxies = []
for y in range(height):
    for x in range(width):
        if image[y][x] == '#':
            galaxies.append((y, x))

# calculate distances between all pairs
# Manhattan distance -> just sum of coordinate differences
one = 0
for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
        iy, ix = galaxies[i]
        jy, jx = galaxies[j]
        distance = abs(iy-jy) + abs(ix-jx)
        one += distance

if 0:
    for l in image:
        print("".join(l))
    print(galaxies)

print('one:', one)
