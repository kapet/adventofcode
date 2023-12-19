import math

data = [line.strip() for line in open('2023/19/input.txt')]
i = data.index('')
workflows = {}
for line in data[:i]:
    name, rest = line.split('{')
    rules = []
    for rule in rest[:-1].split(','):
        if ':' in rule:
            rest, destination = rule.split(':')
            condition = (rest[0], rest[1], int(rest[2:]))
        else:
            condition = None
            destination = rule
        rules.append((condition, destination))
    workflows[name] = rules
parts = []
for line in data[i+1:]:
    values = {}
    for assignment in line[1:-1].split(','):
        values[assignment[0]] = int(assignment[2:])
    parts.append(values)

# Part 1: just execute workflows for given parts
one = 0
for part in parts:
    active = 'in'
    while active != 'A' and active != 'R':
        for condition, destination in workflows[active]:
            if not condition or eval(''.join(map(str, condition)), None, part):
                active = destination
                break
    if active == 'A':
        one += sum(part.values())
print('one:', one)

# Part 2: calculate number of solutions for all input values
two = 0
heap = [
    # start range includes complete input value space
    ('in', {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)})
]
while heap:
    active, values = heap.pop()
    if active == 'A':
        # all parts in the current range are accepted
        two += math.prod(h-l+1 for l,h in values.values())
    elif active != 'R':
        # apply next workflow step to the current range
        for condition, destination in workflows[active]:
            if not condition:
                active = destination
            else:
                c, comp, val = condition
                if comp == '<':
                    if values[c][1] < val:
                        # completely covered
                        active = destination
                        break
                    elif values[c][0] >= val:
                        # completely excluded
                        continue
                    else:
                        # partially covered, split the current range
                        low_values = values.copy()
                        low_values[c] = (values[c][0], val-1)
                        values[c] = (val, values[c][1])
                        heap.append((destination, low_values))
                else: # comp == '>'
                    if values[c][0] > val:
                        # completely covered
                        active = destination
                        break
                    elif values[c][1] <= val:
                        # completely excluded
                        continue
                    else:
                        # partially covered, split the current range
                        high_values = values.copy()
                        high_values[c] = (val+1, values[c][1])
                        values[c] = (values[c][0], val)
                        heap.append((destination, high_values))
        heap.append((active, values))
print('two:', two)


