bags = [l.strip() for l in open('input.txt')]

def prio(char):
    p = ord(char) - (65-27)  # 'A': 65 -> 27
    if p > 52:
        p -= (97-1) - (65-27)  # 'a': 97 -> 1
    return p

summe = 0
for content in bags:
    mid = len(content)//2
    both = set(content[:mid]) & set(content[mid:])
    summe += prio(both.pop())
print('one:', summe)

summe = 0
for i in range(0, len(bags), 3):
    badge = set(bags[i]) & set(bags[i+1]) & set(bags[i+2])
    summe += prio(badge.pop())
print('two:', summe)
