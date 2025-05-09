data = open('2020/22/input.txt').read()
hand1, hand2 = data.split('\n\n')
hand1 = list(map(int, hand1.split('\n')[1:]))
hand2 = list(map(int, hand2.split('\n')[1:]))

p1 = hand1[:]
p2 = hand2[:]
while p1 and p2:
    c1 = p1.pop(0)
    c2 = p2.pop(0)
    if c1 > c2:
        p1.append(c1)
        p1.append(c2)
    else:
        p2.append(c2)
        p2.append(c1)
winner = p1 or p2
one = 0
for i in range(len(winner)):
    one += winner[i] * (len(winner)-i)
print('one', one)


def game(p1, p2):
    seen = set()
    while p1 and p2:
        key = (tuple(p1), tuple(p2))
        if key in seen:
            return '1', p1, p2
        seen.add(key)
        c1 = p1.pop(0)
        c2 = p2.pop(0)
        if len(p1) >= c1 and len(p2) >= c2:
            winner, _, _ = game(p1[:c1], p2[:c2])
        else:
            winner = (c1 > c2) and '1' or '2'
        if winner == '1':
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)
    return p1 and '1' or '2', p1, p2

_, p1, p2 = game(hand1, hand2)
winner = p1 or p2
two = 0
for i in range(len(winner)):
    two += winner[i] * (len(winner)-i)
print('two', two)
