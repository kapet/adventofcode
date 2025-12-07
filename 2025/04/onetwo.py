data = [list(l.strip()) for l in open("2025/04/input.txt")]
w = len(data[0])
h = len(data)

for y in range(h):
    data[y] = ['.'] + data[y] + ['.']
data.insert(0, ['.']*(w+2))
data.append(['.']*(w+2))
w += 2
h += 2

def find(data):
    found = 0
    newdata = [l[:] for l in data]
    for y in range(1, h-1):
        for x in range(1, w-1):
            if data[y][x] == '@':
                adjacent = data[y-1][x-1:x+2] + data[y][x-1:x+2] + data[y+1][x-1:x+2]
                if adjacent.count('@') <= 4:
                    found += 1
                    newdata[y][x] = 'x'
    return found, newdata

t, data = find(data)
two = one = t
while t:
    t, data = find(data)
    two += t
print("one:", one)
print("two:", two)
