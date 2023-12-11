image = [list(line.strip()) for line in open('2023/11/input.txt')]
height = len(image)
width = len(image[0])

# find all galaxies
galaxies = []
for y in range(height):
    for x in range(width):
        if image[y][x] == '#':
            galaxies.append((y, x))

# find empty rows and columns
emptyrows = list(sorted(set(range(height)) - set(g[0] for g in galaxies)))
emptycols = list(sorted(set(range(width)) - set(g[1] for g in galaxies)))

def _expand(n, empty, factor):
    result = []
    inc = 0
    for i in range(n):
        result.append(inc)
        if i in empty:
            inc += factor
    return result

def expanded(factor):
    row_increments = _expand(height, emptyrows, factor-1)
    col_increments = _expand(width, emptycols, factor-1)

    result = []
    for gy, gx in galaxies:
        result.append((gy+row_increments[gy], gx+col_increments[gx]))
    return result

def sum_distances(galaxies):
    result = 0
    n = len(galaxies)
    for i in range(n):
        for j in range(i+1, n):
            (iy, ix), (jy, jx) = galaxies[i], galaxies[j]
            # Manhattan distance
            result += abs(iy-jy) + abs(ix-jx)
    return result

print('one:', sum_distances(expanded(2)))
print('two:', sum_distances(expanded(1_000_000)))
