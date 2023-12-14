platform = [tuple(line.strip()) for line in open('2023/14/input.txt')]

def rotate_cw(data):
    return list(zip(*data[::-1]))

def rotate_ccw(data):
    return list(reversed(list(zip(*data))))

def tilt_left(platform):
    tilted_platform = []
    for line in platform:
        parts = []
        for part in ''.join(line).split('#'):
            # 'O' is sorted before '.'
            parts.append(''.join(sorted(part, reverse=True)))
        tilted_platform.append('#'.join(parts))
    return tilted_platform

def calc_weight_down(platform):
    # this is easiest if north is down
    weight = 0
    for i,l in enumerate(platform, start=1):
        weight += i * l.count('O')
    return weight

# tilting is easier horizontally than vertically, so the loop assumes north is left
platform = rotate_ccw(platform)

one = two = None
seen = {}
weights = []
for cycle in range(5000):
    for i in range(4):
        platform = tilt_left(platform)
        if cycle == 0 and i == 0:
            p = rotate_ccw(platform)
            one = calc_weight_down(p)
        if i == 3:
            # a little hacky to put it here but avoids extra rotations
            weights.append(calc_weight_down(platform))
        platform = rotate_cw(platform)

    # have we seen the exact same platform setup before? yes->cycle
    as_str = ''.join(''.join(l) for l in platform)
    if as_str in seen:
        mu = seen[as_str]
        lam = cycle - mu
        two = weights[mu + (1_000_000_000-mu-1) % lam]
        break
    else:
        seen[as_str] = cycle

print('one:', one)
print('two:', two)
