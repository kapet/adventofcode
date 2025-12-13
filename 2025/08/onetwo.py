import math

data = [[int(i) for i in l.split(',')] for l in open("2025/08/input.txt")]
n = len(data)
stop_one = 10
if n > 20:
    stop_one = 1000

# calculate all edges
edges = []
for i, x in enumerate(data[:-1]):
    for j, y in enumerate(data[i+1:], start=i+1):
        # can ignore math.sqrt for sorting
        distance = (x[0]-y[0])**2 + (x[1]-y[1])**2 + (x[2]-y[2])**2
        edges.append((distance, i, j))
edges.sort()

# Kruskal with lists
group_of_element = list(range(n))
groups = {t: [t,] for t in range(n)}
for i, (_, x, y) in enumerate(edges):
    gx, gy = group_of_element[x], group_of_element[y]
    if gx != gy:
        moving = groups.pop(gy)
        groups[gx].extend(moving)
        for j in moving:
            group_of_element[j] = gx
        if len(groups) == 1:
            print("two", data[x][0]*data[y][0])
            break

    if i == stop_one-1:
        counts = [len(t) for t in groups.values()]
        tops = sorted(counts, reverse=True)[:3]
        print("one", math.prod(tops))
