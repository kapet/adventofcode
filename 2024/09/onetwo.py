import heapq
import itertools

filedata = list(map(int, open('2024/09/input.txt').read().strip()))
#            0   1   2
#filedata = [1,4,1,1,3]

one = []
two_id = []
two_length = []
id = 0
for c, isfile in zip(filedata, itertools.cycle((True, False))):
    if isfile:
        one.extend([id] * c)
        two_id.append(id)
        two_length.append(c)
        id += 1
    elif c > 0:
        one.extend([None] * c)
        two_id.append(None)
        two_length.append(c)

############# PART ONE
dst = 0
src = len(one)-1
while src > dst:
    if one[src] == None:
        src -= 1
        continue
    if one[dst] != None:
        dst += 1
        continue
    one[dst] = one[src]
    one[src] = None
print('one', sum(id*i for i, id in enumerate(one) if id is not None))

############# PART TWO
mindst = 0
src = len(two_id)-1
maxid = two_id[-1] + 1
while src > mindst:
    if two_id[src] is None or two_id[src] >= maxid:
        src -= 1
        continue
    if two_id[mindst] != None:
        mindst += 1
        continue

    for dst in range(mindst, src):
        if two_id[dst] == None and two_length[dst] >= two_length[src]:
            rest = two_length[dst] - two_length[src]
            maxid = two_id[dst] = two_id[src]
            two_id[src] = None
            if rest:
                two_length[dst] = two_length[src]
                two_id.insert(dst+1, None)
                two_length.insert(dst+1, rest)
                src += 1
            break
    else:
        # no space found
        src -= 1
two = []
for id, length in zip(two_id, two_length):
    two.extend([id] * length)
print('two', sum(id*i for i, id in enumerate(two) if id is not None))
