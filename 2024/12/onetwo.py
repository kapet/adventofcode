import collections

mymap = [list(s.strip()) for s in open('2024/12/input.txt')]
w = len(mymap[0])
h = len(mymap)

tagmap = [[0] * w for _ in range(h)]

def _get(y, x):
    if 0 <= y < h and 0 <= x < w:
        return [(mymap[y][x], tagmap[y][x])]
    else:
        return []
    
def neighbors(y, x):
    return _get(y-1, x) + _get(y, x+1) + _get(y+1, x) + _get(y, x-1)

nexttag = 1
area = collections.defaultdict(int)
perimeter = collections.defaultdict(int)
taggroups = collections.defaultdict(list)
for y in range(h):
    for x in range(w):
        c = mymap[y][x]
        mytag = 0
        p = 4
        for n, t in neighbors(y, x):
            if c == n:
                p -= 1
                if t:
                    if mytag and mytag != t:
                        # found two neighbors with same value and different tags, merge their tag groups
                        mykey = (c, mytag)
                        otherkey = (n, t)
                        area[mykey] += area[otherkey]
                        del area[otherkey]
                        perimeter[mykey] += perimeter[otherkey]
                        del perimeter[otherkey]
                        otherfields = taggroups[t]
                        del taggroups[t]
                        taggroups[mytag].extend(otherfields)
                        for oy, ox in otherfields:
                            tagmap[oy][ox] = mytag
                    else:
                        mytag = t
        if not mytag:
            mytag = nexttag
            nexttag += 1
        tagmap[y][x] = mytag
        taggroups[mytag].append((y,x))

        key = (c, mytag)
        area[key] += 1
        if p:
            perimeter[key] += p

one = 0
for c in area.keys():
    one += area[c] * perimeter[c]
print('one', one)


# Part 2 is tricksy. Instead of counting the sides, count the corners - thats the same number.
corners = collections.defaultdict(int)

# outside corners are always a corner
for y, x in [(0,0), (0,w-1), (h-1,w-1), (h-1,0)]:
    corners[tagmap[y][x]] += 1

# outside edges are corners if two neighboring fields differ
for y in range(h-1):
    for x in [0, w-1]:
        t1 = tagmap[y][x]
        t2 = tagmap[y+1][x]
        if t1 != t2:
            corners[t1] += 1
            corners[t2] += 1
for y in [0, h-1]:
    for x in range(w-1):
        t1 = tagmap[y][x]
        t2 = tagmap[y][x+1]
        if t1 != t2:
            corners[t1] += 1
            corners[t2] += 1

# inside is complex
for y in range(0, h-1):
    for x in range(0, w-1):
        t1 = tagmap[y][x]
        t2 = tagmap[y][x+1]
        t3 = tagmap[y+1][x]
        t4 = tagmap[y+1][x+1]
        t = collections.Counter([t1, t2, t3, t4])
        if len(t) == 4:
            # four different tags, they all have a corner!
            t = list(t)
        elif len(t) == 3:
            # three different tags, one uses two fields
            if t1 != t4 and t2 != t3:
                # the tag on two fields is a pair, it has no corner
                t = [t_[0] for t_ in t.most_common()[1:]]
            else:
                # the tag on two fields is set diagonally, has a corner
                t = list(t.elements())
        elif len(t) == 2:
            # two different tags, either 2:2 or 3:1
            tmax = t.most_common(1)[0][1]
            if tmax == 3:
                # its 3:1 with an L-form stone, each tag has one corner
                t = list(t)
            elif t1 != t4 and t2 != t3:
                # its 2:2 with them set in pairs, no corners
                t = []
            else:
                # 2:2 again but checkerboard, each has two corners!
                t = list(t.elements())
        else: # len(t) == 1:
            # all the same tag, we are in the middle of a field, no corners
            t = []
            
        for t_ in t:
            corners[t_] += 1

two = 0
for c in area.keys():
    t = c[1]
    two += area[c] * corners[t]
print('two', two)


# AB   each tag has one outside corner
# CD
#
# AA AB only B and C have a corner, not A
# BC AC
# 
# AA AB  no corners
# BB AB
# 
# AB  A and B both have two corners!
# BA
# 
# AB  B and C have one corner, A has two corners
# CA
# 
# AA  A and B both have one corner
# AB
# 
# AA  no corner
# AA