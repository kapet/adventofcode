cards = []
sep = 0
for line in open('2023/04/input.txt'):
    line = line.split()[2:]
    if not sep:
        sep = line.index('|')
    winning = set(int(i) for i in line[:sep])
    having = set(int(i) for i in line[sep+1:])
    cards.append((winning, having))

ncards = [1]*len(cards)
one = 0
for card, (winning,having) in enumerate(cards):
    n = len(winning & having)
    if n:
        one += 2**(n-1)
        for i in range(card+1, card+1+n):
            ncards[i] += ncards[card]
print('one:', one)
print('two:', sum(ncards))
