lines = [l.strip() for l in open('2023/01/input.txt')]

s = 0
for l in lines:
    l = [c for c in l if c.isdecimal()]
    n = int(l[0] + l[-1])
    s += n
print('one:', s)

# sometimes numbers overlap by one character, so don't remove the strings
# and instead put the digit in the middle, all the characters will be removed
# in a later step anyway
numbers = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
s = 0
for l in lines:
    for n, t in enumerate(numbers, start=1):
        n = t[0] + str(n) + t[1:]
        l = l.replace(t, n)
    l = [c for c in l if c.isdecimal()]
    n = int(l[0] + l[-1])
    s += n
print('two:', s)
