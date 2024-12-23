connections = [l.strip().split("-") for l in open('2024/23/input.txt')]

conns = {}
for c1, c2 in connections:
    conns.setdefault(c1, []).append(c2)
    conns.setdefault(c2, []).append(c1)

triples = set()
for c1 in conns.keys():
    for c2 in conns[c1]:
        for c3 in conns[c2]:
            if c3 != c1:
                for c4 in conns[c3]:
                    if c4 == c1:
                        if c1.startswith('t') or c2.startswith('t') or c3.startswith('t'):
                            triples.add(tuple(sorted((c1, c2, c3))))
print('one', len(triples))

groups = set()
for c1 in conns.keys():
    group = set([c1])
    tested = set([c1])
    to_test = set(conns[c1])
    while to_test:
        c2 = to_test.pop()
        if (c2 not in tested) and all(c2 in conns[c3] for c3 in group):
            group.add(c2)
            to_test |= set(conns[c2])
        tested.add(c2)
    groups.add(tuple(sorted(group)))
two = max(groups, key=len)
print('two', ','.join(two))
