mapping = dict(zip('([{<', ')]}>'))
points = dict(zip(')]}>', (3, 57, 1197, 25137)))

total = 0
for line in open('2021/10/input.txt'):
    stack = []
    for c in line.strip():
        if c in '([{<':
            stack.append(c)
        else:
            s = stack.pop()
            if mapping[s] != c:
                total += points[c]

print(total)
