# digit - number of segments / length of string
#     0 - 6
#     1 - 2 unique and smallest
#     2 - 5
#     3 - 5
#     4 - 4 unique
#     5 - 5
#     6 - 6
#     7 - 3 unique
#     8 - 7 unique and biggest
#     9 - 6

# with all digits
# segment - digits     - sum
#       a - 0 23 56789 - 8
#       b - 0   456 89 - 6
#       c - 01234  789 - 8
#       d -   23456 89 - 7
#       e - 0 2   6 8  - 4
#       f - 01 3456789 - 9
#       g - 0 23 56 89 - 7

# after removing digits 1,4,7,8
# segment - digits - sum
#       a - 023569 - 6   
#       b - 0  569 - 4   
#       c - 023  9 - 4   
#       d -  23569 - 5   
#       e - 02  6  - 3   
#       f - 0 3569 - 5   
#       g - 023569 - 6   

# sums concatenated
# a - 86
# b - 64
# c - 84
# d - 75
# e - 43
# f - 95
# g - 76

segment_ids = {'86': 'a', '64': 'b', '84': 'c', '75': 'd',
               '43': 'e', '95': 'f', '76': 'g'}

import collections

class Entry:
    def __init__(self, line):
        line = line.split()
        self.patterns = line[:10]
        self.outputs = line[11:]

data = [Entry(line) for line in open('2021/08/input.txt')]

total = 0
for e in data:
    digits = [None]*10

    # sort characters in patterns, and patterns by length
    patterns = map(lambda p: ''.join(sorted(p)), e.patterns)
    patterns = sorted(patterns, key=lambda x: len(x))

    # patterns now of length: 2 3 4 5 5 5 6 6 6 7
    # just pick the obvious digits
    digits[1] = patterns[0]
    digits[7] = patterns[1]
    digits[4] = patterns[2]
    digits[8] = patterns[-1]

    # count frequency of individual segments, first in whole set,
    # then in the remaining set after removing the known digits,
    first_freq = collections.Counter(''.join(patterns)).most_common()
    second_freq = collections.Counter(''.join(patterns[3:-1])).most_common()

    # combine both frequencies to get a unique id per segment, look it up,
    # and then put it all into a dict mapping official segment id -> bad one
    segments = {}
    for t1, t2 in zip(sorted(first_freq), sorted(second_freq)):
        segments[segment_ids[str(t1[1])+str(t2[1])]] = t1[0]

    # now we can just build the remaining digits :-)
    def build_digit(s):
        return ''.join(sorted(segments[i] for i in s))

    digits[0] = build_digit('abcefg')
    digits[2] = build_digit('acdeg')
    digits[3] = build_digit('acdfg')
    digits[5] = build_digit('abdfg')
    digits[6] = build_digit('abdefg')
    digits[9] = build_digit('abcdfg')

    # know all digits now, so get outputs and sort chars in digits
    outputs = map(lambda o: ''.join(sorted(o)), e.outputs)
    # lookup each digit and build result
    outputs = [str(digits.index(o)) for o in outputs]
    output = int(''.join(outputs))

    total += output

print(total)