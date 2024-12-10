mymap = []
for l in open('2024/10/input.txt'):
    mymap.append(list(map(int, l.strip())))
w = len(mymap[0])
h = len(mymap)

def destinations(y, x, i):
    if not (0 <= y < h) or not (0 <= x < w) or mymap[y][x] != i:
        return []
    elif i == 9:
        return [(y,x)]
    else:
        return destinations(y-1, x, i+1) + destinations(y, x+1, i+1) + destinations(y+1, x, i+1) + destinations(y, x-1, i+1)

one = two = 0
for y in range(h):
    for x in range(w):
        if mymap[y][x] == 0:
            d = destinations(y, x, 0)
            one += len(set(d))
            two += len(d)
print('one', one)
print('two', two)