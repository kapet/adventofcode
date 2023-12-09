histories = [list(map(int, line.split())) for line in open('2023/09/input.txt')]

def reduce(history):
    return [history[i+1] - history[i] for i in range(len(history)-1)]

one = two = 0
for history in histories:
    lines = [history]
    while any(lines[-1]):
        lines.append(reduce(lines[-1]))

    forward = backward = 0
    for line in reversed(lines):
        forward = line[-1] + forward
        backward = line[0] - backward
    one += forward
    two += backward
    print(forward, backward)
print('one:', one)
print('two:', two)
