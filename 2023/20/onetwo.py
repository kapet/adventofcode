import collections
import math

configs = {}
for line in open('2023/20/input.txt'):
    line = line.split()
    name = line[0]
    if name == 'broadcaster':
        type_ = 'b'
    else:
        type_ = name[0]
        name = name[1:]
    destinations = tuple(d.strip(',') for d in line[2:])
    configs[name] = (type_, destinations)

inputs = collections.defaultdict(list)
for name, (_, destinations) in configs.items():
    for dest in destinations:
        inputs[dest].append(name)

LOW = OFF = False
HIGH = ON = True

# A little brute forcing attempt did not go anywhere.
# See rx.py, rx.png, and rx.txt for steps to figure out what is going
# on with the graph - there are four 'counters' implemented with
# flipflops. They produce four cycles with different intervals, so
# the solution for part 2 is to detect those intervals and then
# calculate the LCM.
assert 'rx' not in configs
assert inputs['rx'] == ['qt']
two_cycles = {k:[] for k in inputs['qt']}

one = {LOW: 0, HIGH: 0}
flipflop_states = {}
conjunction_states = {n: {k:LOW for k in s} for n, s in inputs.items()}
n = 1
while n <= 1000 or not all(len(t) for t in two_cycles.values()):
    heap = [(LOW, 'button', 'broadcaster')]
    while heap:
        pulse, source, name = heap.pop(0)
        one[pulse] += 1
        if pulse and name == 'qt':
            two_cycles[source].append(n)

        if name not in configs:
            continue
        type_, destinations = configs[name]

        if type_ == '%':
            if pulse:  # HIGH -> ignore
                continue
            pulse = flipflop_states[name] = not flipflop_states.get(name, OFF)
        elif type_ == '&':
            state = conjunction_states[name]
            state[source] = pulse
            pulse = not all(state.values()) # HIGH if any one is LOW
        for dest in destinations:
            heap.append((pulse, name, dest))

    if n == 1000:
        print('one:', one[LOW] * one[HIGH])
    n += 1

def lcm(a, b):
    return a*b // math.gcd(a, b)

# two_values now includes the number of button presses until each of
# the individual counters triggered the expected output signal.
two_values = [v[0] for v in two_cycles.values()]
two = two_values[0]
for v in two_values[1:]:
    two = lcm(two, v)
print('two:', two)
