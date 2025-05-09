import itertools

numbers = [int(l) for l in open('2020/09/input.txt')]
preamble = 25

for i in range(preamble, len(numbers)):
    n = numbers[i-preamble:i]
    ok = set(a+b for a,b in itertools.combinations(n, 2))
    if numbers[i] not in ok:
        one = numbers[i]
        break
print('one', one)

a = b = 0
n = numbers[0]
while n != one:
    while n < one:
        b += 1
        n += numbers[b]
    while n > one:
        n -= numbers[a]
        a += 1
print('two', min(numbers[a:b+1])+max(numbers[a:b+1]))