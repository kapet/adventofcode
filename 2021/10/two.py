mapping = dict(zip('([{<', ')]}>'))
points = dict(zip('([{<', (1, 2, 3, 4)))

scores = []
for line in open('2021/10/input.txt'):
    total = 0
    stack = []
    for c in line.strip():
        if c in '([{<':
            stack.append(c)
        else:
            s = stack.pop()
            if mapping[s] != c:
                # line is corrupted, skip it
                stack = []
                break
    while stack:
        s = stack.pop()
        total = total*5 + points[s]
    if total:
        scores.append(total)

print(sorted(scores)[len(scores)//2])
