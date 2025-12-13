data = [[int(i) for i in l.split(',')] for l in open("2025/09/input.txt")]
n = len(data)

print("Find all possible rectangles and their size")
w = 0
h = 0
areas = []
for i, x in enumerate(data[:-1]):
    for j, y in enumerate(data[i+1:], start=i+1):
        w = max(w, x[0], y[0])
        h = max(h, x[1], y[1])
        area = (abs(x[1]-y[1])+1) * (abs(x[0]-y[0])+1)
        areas.append((area, i, j))
areas.sort()
print("one", areas[-1][0])
h += 1
w += 1

print("Put all points on a map")
map_ = {}
for x, y in data:
    map_.setdefault(y, {})[x] = '#'
rows = tuple(sorted(map_.keys()))
cols = tuple(sorted(set(c for r in map_.values() for c in r.keys())))

print("Draw the edges on the map")
def _line(i, j):
    i, j = data[i], data[j]
    if i[0] == j[0]:
        x = i[0]
        ys = rows.index(min(i[1], j[1]))
        ye = rows.index(max(i[1], j[1]))
        for y in rows[ys+1:ye]:
            map_[y][x] = 'X'
    else:
        assert i[1] == j[1]
        y = i[1]
        xs = cols.index(min(i[0], j[0]))
        xe = cols.index(max(i[0], j[0]))
        for x in cols[xs+1:xe]:
            map_[y][x] = 'X'
for i in range(len(data)-1):
    _line(i, i+1)
_line(-1, 0)

# Write to file in compact format. This showed that the figure has no
# lines crossing each other, no holes, and no "semi-holes".
if 0:
    with open("2025/09/output.txt", "wt") as f:
        for r in brows:
            f.write(''.join(map_[r].get(c, '.') for c in bcols) + '\n')

print("Add an empty border and flood-fill from the outside")
brows = [rows[0]-1] + list(rows) + [rows[-1]+1]
bcols = [cols[0]-1] + list(cols) + [cols[-1]+1]
flood = {(0, 0)}
while flood:
    c, r = flood.pop()
    if map_.get(brows[r], {}).get(bcols[c], '.') == '.':
        map_.setdefault(brows[r], {})[bcols[c]] = ' '
        if r-1 >= 0:
            flood.add((c, r-1))
        if c-1 >= 0:
            flood.add((c-1, r))
        if r+1 < len(brows):
            flood.add((c, r+1))
        if c+1 < len(bcols):
            flood.add((c+1, r))

print("Find biggest rect that has no outside field inside itself")
for area, i, j in reversed(areas):
    i = data[i]
    j = data[j]
    ys = rows.index(min(i[1], j[1]))
    ye = rows.index(max(i[1], j[1]))
    xs = cols.index(min(i[0], j[0]))
    xe = cols.index(max(i[0], j[0]))
    # quick check: any corners outside?
    l1, l2 = map_[rows[ys]], map_[rows[ye]]
    if l1.get(xs)==' ' or l1.get(xe)==' ' or l2.get(xs)==' ' or l2.get(xe)==' ':
        continue
    # full check. TODO: maybe just check border?
    fail = False
    for y in rows[ys:ye+1]:
        for x in cols[xs:xe+1]:
            if map_[y].get(x, '.') == ' ':
                fail = True
                break
        if fail:
            break
    if not fail:
        print("two", area)
        break

