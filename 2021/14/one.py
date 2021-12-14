import collections

with open('2021/14/test.txt') as f:
    template = f.readline().strip()
    _ = f.readline()
    rules = dict([l.strip().split(' -> ') for l in f])

print('got template size {} and {} rules'.format(len(template), len(rules)))

poly = list(template)
for step in range(1, 11):
    prev = poly[0]
    new_poly = [prev]
    for i in range(1, len(poly)):
        this = poly[i]
        ins = rules.get(prev+this, None)
        if ins:
            new_poly.append(ins)
        new_poly.append(this)
        prev = this
    poly = new_poly

    stats = collections.Counter(poly)
    common = stats.most_common()
    answer = common[0][1] - common[-1][1]
    print('after step {}: length {}, {}, answer={}'.format(step, len(poly), stats, answer))