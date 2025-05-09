mymap = [list(l.strip()) for l in open('2020/03/input.txt')]
w = len(mymap[0])
h = len(mymap)

def test(right, down):
    result = x = y = 0
    while y < h:
        if mymap[y][x] == '#':
            result += 1
        x = (x + right) % w
        y += down
    return result

one = test(3, 1)
print('one', one)

two = test(1, 1) * one * test(5, 1) * test(7, 1) * test(1, 2)
print('two', two) 