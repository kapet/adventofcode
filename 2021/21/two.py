import collections
import itertools

start_test = [4, 8]
start_input = [1, 3]

# 3 sided die, splitting the universe
# rolled 3 times: 3x3x3 = 27 possibilities in 27 universes after starting from one starting point
# but not 27 different sums! can count how many universes move for 3..9 steps each, only 7 different options
rolls = itertools.product((1,2,3), repeat=3)
steps = collections.Counter(sum(t) for t in rolls)

# each roll only splits the current users' universe, all 27 new universes inherit the same other player situation
# if only tracking live universes, then analyzing one players state means that every known universe of the other player has not yet finished

# pawns currently on the same field in different universes can have different points, need to use position+points to identify

# therefore need to track number of universes per (position, points) for each player separately
#     universes[player 0..1][position 0..9][points 0..20]
def empty_player():
    return [[0]*21 for _ in range(10)]
universes = [empty_player(), empty_player()]

# initialize start positions, just one universe for each player
pos = start_input
universes[0][pos[0]-1][0] = 1
universes[1][pos[1]-1][0] = 1
totals = [0, 0]

player = 1
for step in range(21):
    player = 1-player
    total_other_universes = sum(sum(t) for t in universes[1-player])
    new = empty_player()
    # iterate through all universe data for the current player
    for position in range(10):
        for points in range(21):
            existing_universes = universes[player][position][points]
            # iterate through all possible die roll outcomes
            for increment, children in steps.items():
                # the universes at (position, points) are moved forward by increment and get split into children new universes
                newposition = (position + increment) % 10
                newpoints = points + (newposition + 1)
                newuniverses = existing_universes * children
                if newpoints >= 21:
                    # these child universes have completed, do not need to track them any more
                    # all the opposite players universes lose (but only for these children, not for other die results)
                    totals[player] += newuniverses * total_other_universes
                else:
                    # not there yet, keep their state in mind
                    new[newposition][newpoints] += newuniverses
    universes[player] = new

print(totals)
