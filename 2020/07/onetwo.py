import functools

rules = {}
for l in open('2020/07/input.txt'):
    l = l.split()
    outside = ' '.join(l[0:2])
    if l[4] == 'no':
        inside = []
    else:
        inside = [(int(l[i]), ' '.join(l[i+1:i+3])) for i in range(4, len(l), 4)]
    rules[outside] = inside

can_be_in = {}
for key, values in rules.items():
    for _, color in values:
        can_be_in.setdefault(color, []).append(key)

stack = ['shiny gold']
one = set()
while stack:
    color = stack.pop(0)
    if color in one:
        continue
    one.add(color)
    if color in can_be_in:
        stack.extend(can_be_in[color])
print('one', len(one)-1)

@functools.cache
def count(color):
    if not rules[color]:
        return 1
    else:
        return 1 + sum(i*count(c) for i, c in rules[color])

print('two', count('shiny gold') - 1)
