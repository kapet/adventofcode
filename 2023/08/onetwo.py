import math

sequence = None
elements = {}
for i, line in enumerate(open('2023/08/input.txt')):
    if i == 0:
        sequence = line.strip()
    elif i >= 2:
        e, _, l, r = line.split()
        elements[e] = (l[1:-1], r[:-1])

def steps(element, goals):
    i = 0
    while element not in goals:
        step = sequence[i%len(sequence)]
        element = elements[element][step=='R' and 1 or 0]
        i += 1
    return i

if 'AAA' in elements:
    print('one:', steps('AAA', set(('ZZZ',))))

# from poking at the data a bit:
# -> same number of start as end elements
# -> every start element always leads to only one target element
# -> there are loops of multiples of the sequence length
# -> distance from start to first target is same as from target to target
# therefore I can just figure out the steps to the first time each start
# element takes to hit the target, and then calculate the least common
# multiple of all those individual lengths.

def lcm(a, b):
    return a*b // math.gcd(a, b)

element = [e for e in elements.keys() if e.endswith('A')]
finish = set(e for e in elements.keys() if e.endswith('Z'))
element_steps = [steps(e, finish) for e in element]
two = element_steps[0]
for es in element_steps[1:]:
    two = lcm(two, es)
print('two:', two)
