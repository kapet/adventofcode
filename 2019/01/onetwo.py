import functools

@functools.cache
def fuel(mass):
    return (mass // 3) - 2

one = 0
two = 0
for l in open('2019/01/input.txt'):
    l = int(l)
    l = fuel(l)
    one += l
    while l > 0:
        two += l
        l = fuel(l)
print('one', one)
print('two', two)
