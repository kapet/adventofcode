grid = []
for line in open('input.txt'):
    grid.append([int(l) for l in line.strip()])

h = len(grid)
w = len(grid[0])

# build a map of sightlines. A '2' in this map means that the smallest tree in any sightline has height '2'.
visible_height = [[9]*w for _ in range(h)]
for i in range(h):
    left = 0
    right = 0
    for j in range(w):
        visible_height[i][j] = min(visible_height[i][j], left)
        visible_height[i][-1-j] = min(visible_height[i][-1-j], right)
        left = max(grid[i][j], left)
        right = max(grid[i][-1-j], right)
for j in range(w):
    top = 0
    bottom = 0
    for i in range(h):
        visible_height[i][j] = min(visible_height[i][j], top)
        visible_height[-1-i][j] = min(visible_height[-1-i][j], bottom)
        top = max(grid[i][j], top)
        bottom = max(grid[-1-i][j], bottom)

# the outside is completely visible, as is every tree sticking out above visibility sightlines
visible = w+w+2*(h-2)
for y in range(1, h-1):
    for x in range(1, w-1):
        if grid[y][x] > visible_height[y][x]:
            visible += 1
print('one:', visible)


# build a map of scenic scores. This is the viewing distances in each direction multiplied.
scenic_score = [[1]*w for _ in range(h)] # init with 1 so we can multiply with it
for i in range(1, h-1):
    left = [1]*10 # distances for every height to the left
    right = [1]*10
    for j in range(1, w-1):
        lh = grid[i][j]
        rh = grid[i][-1-j]
        scenic_score[i][j] *= left[lh]
        scenic_score[i][-1-j] *= right[rh]
        # now update distances based on current position height
        for t in range(10):
            if t <= lh:
                left[t] = 1
            else:
                left[t] += 1
            if t <= rh:
                right[t] = 1
            else:
                right[t] += 1
for j in range(1, w-1):
    top = [1]*10 # distances for every height to the top
    bottom = [1]*10
    for i in range(1, h-1):
        th = grid[i][j]
        bh = grid[-1-i][j]
        scenic_score[i][j] *= top[th]
        scenic_score[-1-i][j] *= bottom[bh]
        # now update distances based on current position height
        for t in range(10):
            if t <= th:
                top[t] = 1
            else:
                top[t] += 1
            if t <= bh:
                bottom[t] = 1
            else:
                bottom[t] += 1

print('two:', max(max(row) for row in scenic_score))
