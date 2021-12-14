import collections
import itertools

if not hasattr(itertools, 'pairwise'):
    # only exists in Py 3.10+, this is from the Python docs:
    def pairwise(iterable):
        # pairwise('ABCDEFG') --> AB BC CD DE EF FG
        a, b = itertools.tee(iterable)
        next(b, None)
        return zip(a, b)
    itertools.pairwise = pairwise

with open('2021/14/input.txt') as f:
    template = f.readline().strip()
    _ = f.readline()
    rules = [l.strip().split(' -> ') for l in f]
rules = dict([(tuple(p), n) for p, n in rules])

print('got template size {} and {} rules'.format(len(template), len(rules)))

# 40 steps gets way too big as the polymer grows exponentially
# but there is no need to store the full sequence, a count of pairs is enough to simulate the growth phase
pairs = collections.Counter(itertools.pairwise(template))
# remember the very last character for stats
last = template[-1]

for step in range(1, 41):
    new_pairs = collections.Counter()
    for pair, n in pairs.items():
        if pair in rules:
            # expand template by splitting the pair and submitting to new pairs
            c0, c2 = pair
            c1 = rules[pair]
            new_pairs[(c0, c1)] += n
            new_pairs[(c1, c2)] += n
        else:
            # no rule for this pair, carry it forward unchanged
            new_pairs[pair] += n
    pairs = new_pairs

    if step % 10 == 0:
        chars = collections.Counter()
        chars[last] = 1
        for pair, n in pairs.items():
            chars[pair[0]] += n
        common = chars.most_common()
        answer = common[0][1] - common[-1][1]
        print('after step {}: {}'.format(step, answer))