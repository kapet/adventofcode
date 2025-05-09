def seat_id(code):
    row = int(code[:7].replace('B', '1').replace('F', '0'), 2)
    col = int(code[7:].replace('R', '1').replace('L', '0'), 2)
    return row*8+col

data = [l.strip() for l in open('2020/05/input.txt')]
all_id = [seat_id(code) for code in data]
all_id.sort()

print('one', all_id[-1])
print('two', [a+1 for a,b in zip(all_id, all_id[1:]) if b-a>1])
