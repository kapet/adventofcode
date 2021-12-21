start_test = [4, 8]
start_input = [1, 3]

_die = 0
die_rolls = 0
def roll():
    global _die, die_rolls
    _die += 1
    if _die == 101:
        _die = 1
    die_rolls += 1
    return _die

pos = start_input
i = 0
totals = [0, 0]
while True:
    pos[i] += roll()+roll()+roll()
    while pos[i] > 10:
        pos[i] -= 10
    totals[i] += pos[i]
    if totals[i] >= 1000:
        break
    print('Player {} rolls and moves to space {} for a total score of {}.'.format(i+1, pos[i], totals[i]))
    i = 1-i

print('Player {} won with {} points.'.format(i+1, totals[i]))
print('Losing player had {} points, total rolls {} => {}'.format(totals[1-i], die_rolls, totals[i-1]*die_rolls))