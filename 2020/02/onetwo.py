import re

m = re.compile(r'(\d+)-(\d+) (.): (.+)$')
data = [m.match(l).groups() for l in open('2020/02/input.txt')]

one = 0
for nmin, nmax, letter, password in data:
    nmin = int(nmin)
    nmax = int(nmax)
    if nmin <= password.count(letter) <= nmax:
        one += 1
print('one', one)

two = 0
for p1, p2, letter, password in data:
    p1 = int(p1)-1
    p2 = int(p2)-1
    if (password[p1] == letter) ^ (password[p2] == letter):
        two += 1
print('two', two)