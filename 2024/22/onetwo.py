import collections
import functools

numbers = [int(l) for l in open('2024/22/input.txt')]

@functools.cache
def next_number(n):
    n = (n ^ (n << 6)) & 0xffffff
    n = (n ^ (n >> 5)) & 0xffffff
    n = (n ^ (n << 11)) & 0xffffff
    return n

def sequence(n):
    result = [n%10]
    for _ in range(2000):
        n = next_number(n)
        result.append(n%10)
    return (n, result)

one = 0
gains = collections.Counter()
for n in numbers:
    nn, s = sequence(n)
    one += nn

    d = [s[i+1]-s[i] for i in range(len(s)-1)]
    g = set()
    for i in range(len(s)-4):
        key = (d[i],d[i+1],d[i+2],d[i+3])
        if key not in g:
            g.add(key)
            gains[key] += s[i+4]

print('one', one)

key, val = gains.most_common(1)[0]
print('two', val, key)
