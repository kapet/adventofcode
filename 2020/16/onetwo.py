fields = {}
ticket = []
nearby = []

with open('2020/16/input.txt') as f:
    while l := f.readline().strip():
        name, l = l.split(':')
        r1, _, r2 = l.split()
        vals = []
        for r in (r1, r2):
            start, end = [int(i) for i in r.split('-')]
            vals.append(range(start, end+1))
        fields[name] = vals

    f.readline() # "your ticket"
    ticket = [int(i) for i in f.readline().strip().split(',')]
    f.readline()

    f.readline() # "nearby tickets"
    while l := f.readline().strip():
        nearby.append([int(i) for i in l.strip().split(',')])

# Filter out invalid nearby tickets
all_ranges = []
for f in fields.values():
    all_ranges.extend(f)
invalid = []
good_nearby = []
for n in nearby:
    is_valid = True
    for m in n:
        for r in all_ranges:
            if m in r:
                break
        else:
            invalid.append(m)
            is_valid = False
    if is_valid:
        good_nearby.append(n)
print('one', sum(invalid))
nearby = good_nearby

# identify which field can not be at some position
mapping = {}
for f in fields.keys():
    mapping[f] = [True] * len(ticket)
for n in nearby:
    for i, m in enumerate(n):
        for fn, frs in fields.items():
            ok = False
            for r in frs:
                if m in r:
                    ok = True
            if not ok:
                mapping[fn][i] = False

# figure out which field must be at which index
# starting with fields that have only one option, then mark
# this index as used in all other fields
fieldmappings = {}
while True:
    i = None
    for f in fields.keys():
        if sum(mapping[f]) == 1:
            i = mapping[f].index(True)
            fieldmappings[f] = i
            break
    
    if i is None:
        break

    for f in fields.keys():
        mapping[f][i] = False

two = 1
for f in fields.keys():
    if f.startswith('departure'):
        two *= ticket[fieldmappings[f]]
print('two', two)
