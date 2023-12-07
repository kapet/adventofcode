import collections

hands = [line.split() for line in open('2023/07/input.txt')]

# n diff cards | n most card | strength
#      1       |      5      |     8          five of a kind
#      2       |      4      |     6          four of a kind
#      2       |      3      |     5          full house
#      3       |      3      |     4          three of a kind
#      3       |      2      |     3          two pair
#      4       |      2      |     2          one pair
#      5       |      1      |     0          high card

values = '23456789TJQKA'
values_joker = 'J23456789TQKA'

def eval_hand(cards, jokers=False):
    assert len(cards) == 5
    
    counted_cards = collections.Counter(cards).most_common()
    if jokers and 'J' in cards and len(counted_cards) > 1:
        # add jokers to the most frequent card
        i = [t[0] for t in counted_cards].index('J')
        _, jokers = counted_cards.pop(i)
        c, n = counted_cards.pop(0)
        counted_cards.insert(0, (c, n+jokers))
    strength = counted_cards[0][1] - len(counted_cards) + 4

    card_values = jokers and values_joker or values
    for c in cards:
        strength = strength*16 + card_values.index(c)
    return strength

evaluated_hands = []
for cards, bid in hands:
    evaluated_hands.append((eval_hand(cards), eval_hand(cards, True), int(bid)))

evaluated_hands.sort(key=lambda t: t[0])
one = 0
for rank, (_, _, bid) in enumerate(evaluated_hands, 1):
    one += rank * bid
print('one:', one)

evaluated_hands.sort(key=lambda t: t[1])
two = 0
for rank, (_, _, bid) in enumerate(evaluated_hands, 1):
    two += rank * bid
print('two:', two)
