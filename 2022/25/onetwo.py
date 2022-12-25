def snafuToInt(snafu):
    base = 1
    value = 0
    for c in reversed(snafu):
        if c == '-':
            c = -1
        elif c == '=':
            c = -2
        else:
            c = int(c)
        value += c * base
        base *= 5
    return value

def intToSnafu(value):
    chars = ['=', '-', '0', '1', '2']
    snafu = []
    while value:
        value, rest = divmod(value+2, 5)
        snafu.insert(0, chars[rest])
    return ''.join(snafu)

test_values = [
    ('1', 1),
    ('2', 2),
    ('1=', 3),
    ('1-', 4),
    ('10', 5),
    ('11', 6),
    ('12', 7),
    ('2=', 8),
    ('1=11-2', 2022),
    ('1121-1110-1=0', 314159265),
]

for snafu, value in test_values:
    assert snafuToInt(snafu) == value
    assert intToSnafu(value) == snafu

total = 0
for line in open('2022/25/input.txt'):
    total += snafuToInt(line.strip())
print('one:', total, intToSnafu(total))
