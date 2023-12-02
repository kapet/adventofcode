data = {}
for line in open('2023/02/input.txt'):
    game, picks = line.split(':')
    game = int(game.split()[1])
    for pick in picks.split(';'):
        vector = [0,0,0]
        for color in pick.split(','):
            n, color = color.split()
            n = int(n)
            match color.strip():
                case 'red':
                    vector[0] = n
                case 'green':
                    vector[1] = n
                case 'blue':
                    vector[2] = n
                case _:
                    raise Exception()
        data.setdefault(game, []).append(vector)

bag = [12, 13, 14]

one = 0
two = 0
for game, picks in data.items():
    fewest = [max(t) for t in zip(*picks)]
    if all(a <= b for a,b in zip(fewest, bag)):
        one += game
    two += fewest[0] * fewest[1] * fewest[2]
print('one:', one)
print('two:', two)
