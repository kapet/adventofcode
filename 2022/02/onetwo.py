guide = []
for l in open('input.txt'):
    guide.append(l.strip().split())

scores = {
    # opponent: {me}    
    'A': {'A': 1+3, 'B': 2+6, 'C': 3+0},
    'B': {'A': 1+0, 'B': 2+3, 'C': 3+6},
    'C': {'A': 1+6, 'B': 2+0, 'C': 3+3},
}

score = 0
lookup = {'X': 'A', 'Y': 'B', 'Z': 'C'}
for opp, me in guide:
    me = lookup[me] # convert XYZ to ABC
    score += scores[opp][me]
print('one:', score)

score = 0
lookup = {
    # goal: {opponent: me}
    'X': {'A': 'C', 'B': 'A', 'C': 'B'}, # goal is losing
    'Y': {'A': 'A', 'B': 'B', 'C': 'C'}, # goal is a draw
    'Z': {'A': 'B', 'B': 'C', 'C': 'A'}, # goal is winning
}
for opp, goal in guide:
    me = lookup[goal][opp]
    score += scores[opp][me]
print('two:', score)
