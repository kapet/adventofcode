assignments = []
for line in open('input.txt'):
    pair = []
    for elf in line.strip().split(','):
        pair.append(tuple(int(v) for v in elf.split('-')))
    assignments.append(pair)

def contains(one, two):
    # is two fully contained in one?
    return one[0]<=two[0] and one[1]>=two[1]

overlaps = 0
for one,two in assignments:
    if contains(one, two) or contains(two, one):
        overlaps += 1
print('one:', overlaps)

def leftof(one, two):
    # is one completely to the left of two?
    # assumes v[1] >= v[0]
    return one[1] < two[0]

overlaps = 0
for one,two in assignments:
    if leftof(one, two) or leftof(two, one):
        # they don't overlap at all
        pass
    else:
        overlaps += 1
print('two:', overlaps)
