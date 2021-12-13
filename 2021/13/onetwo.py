dots = []
folds = []
for line in open('2021/13/input.txt'):
    if ',' in line:
        dots.append(tuple(map(int, line.strip().split(','))))
    elif line.startswith('fold along'):
        axis, i = line.strip()[11:].split('=')
        folds.append((axis, int(i)))
    else:
        print('skipping line: ' + line.strip())

print('got {} dots and {} folds'.format(len(dots), len(folds)))

for fold_axis, fold_line in folds:
    folded_dots = set()  # using a set to auto-dedup
    for x,y in dots:
        if fold_axis == 'x':
            if x > fold_line:
                x = fold_line - (x-fold_line)
        else:
            if y > fold_line:
                y = fold_line - (y-fold_line)
        folded_dots.add((x, y))
    dots = folded_dots
    print('after folding along {}={} have {} dots'.format(fold_axis, fold_line, len(dots)))

width = 1+max(dots, key=lambda t: t[0])[0]
height = 1+max(dots, key=lambda t: t[1])[1]
output = [[' ']*width for _ in range(height)]
for x,y in dots:
    output[y][x] = '#'
print('\n'.join(''.join(o) for o in output))