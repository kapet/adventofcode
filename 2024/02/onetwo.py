data = [list(map(int, l.split())) for l in open('2024/02/input.txt').readlines()]


def check(line):
    diffs = [t[1]-t[0] for t in zip(line, line[1:])]
    return all(1 <= abs(t) <= 3 for t in diffs) and (all(t > 0 for t in diffs) or all(t < 0 for t in diffs))


safe1 = 0
safe2 = 0
for line in data:
    if check(line):
        safe1 += 1
        continue

    for i in range(len(line)):
        l = line[:]
        del l[i]
        if check(l):
            safe2 += 1
            break

print('one:', safe1)
print('two:', safe1 + safe2)
