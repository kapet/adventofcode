# read file, get rid of \n
data = [l.strip() for l in open('2021/04/input.txt')]

# first line is numbers being drawn
numbers_drawn = [int(i) for i in data[0].split(',')]

# rest of file is boards: one empty line followed by 5 lines with numbers
boards = []
for i in range(1, len(data)-1, 6):
    board = []
    for j in range(1, 6):
        board.append([int(t) for t in data[i+j].split()])
    boards.append(board)

print('got {} draws and {} boards'.format(len(numbers_drawn), len(boards)))

# create a table of data to track how many hits we've had in each row and column,
# also calculate a 'total' score for each board
# also create an inverse mapping to find all boards quickly that have some number
mapping = {}
table = []
for board in range(len(boards)):
    data = {
        'score':  0,
        'rows': [0]*5,
        'cols': [0]*5,
    }
    for row in range(5):
        for col in range(5):
            value = boards[board][row][col]

            data['score'] += value
            mapping.setdefault(value, []).append((board, row, col))
    table.append(data)

# now just iterate through drawn numbers and update table accordingly
bingo = False
for nr in numbers_drawn:
    # use .get(,[]) in case no board has nr
    for (board, row, col) in mapping.get(nr, []):
        # update the boards score
        table[board]['score'] -= nr
        # track which rows and columns have had hits and check if bingo
        table[board]['rows'][row] += 1
        if table[board]['rows'][row] == 5:
            bingo = True
            break

        table[board]['cols'][col] += 1
        if table[board]['cols'][col] == 5:
            bingo = True
            break

    if bingo:
        final_score = table[board]['score'] * nr
        break

assert bingo
print('bingo on board {}, final score {}'.format(board, final_score))