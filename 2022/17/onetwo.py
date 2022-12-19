input_test = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'
input_full = open('2022/17/input.txt').read().strip()
jets = input_full
jets_index = 0

rocks = [
    (0b00111100,),
    (0b00010000, 0b00111000, 0b00010000),
    (0b00111000, 0b00001000, 0b00001000),  # reversed!
    (0b00100000, 0b00100000, 0b00100000, 0b00100000),
    (0b00110000, 0b00110000)
]
rocks_index = 0

height = 1  # line 0 is the 'ground'
chamber = [0b111111111]  # 9 bits! 7 for the content, 1 each side for the wall
rock = None
number_of_rocks = 0
while True:
    if not rock:
        rock = rocks[rocks_index]
        rocks_index = (rocks_index+1) % len(rocks)

        rock_y = height + 3
        for i in range(rock_y + len(rock) - len(chamber)):
            chamber.append(0b100000001)
    
    # STEP 1: rock being pushed by jet
    jet = jets[jets_index]
    jets_index = (jets_index+1) % len(jets)
    assert jet in '<>'
    if jet == '<':
        shift = int.__lshift__
    else:
        shift = int.__rshift__
    new_rock = [shift(t, 1) for t in rock]
    for i in range(len(rock)):
        if new_rock[i] & chamber[rock_y+i]:
            # pushed into a wall
            break
    else:
        # no conflict with a wall
        rock = new_rock

    # STEP 2: rock falling down
    new_rock_y = rock_y - 1
    for i in range(len(rock)):
        if rock[i] & chamber[new_rock_y+i]:
            # fell onto something
            for j in range(len(rock)):
                chamber[rock_y+j] |= rock[j]
            height = max(height, rock_y + len(rock))
            rock = None
            break
    else:
        # free to go one down
        rock_y = new_rock_y

    if 0:
        for i in range(len(chamber)-1, 0, -1):
            line = bin(chamber[i])
            line = '|' + line[3:-1].replace('0', ' ').replace('1', '#') + '|'
            print(line)
        print('+-------+')
        print()

    if rock == None:
        number_of_rocks += 1
        if number_of_rocks == 2022:
            print('one:', height-1)
            break


