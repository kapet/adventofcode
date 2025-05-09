data = open('2020/15/input.txt').read().strip()
#data = '3,1,2'

data = [int(i) for i in data.split(',')]

previously = {}
i = 0

for n in data:
    i += 1
    previously[n] = i

# in the test and input sets, the last start number is always a first
n = 0
while True:
    i += 1
    if i == 2020:
        print('one', n)
    elif i == 30000000:
        print('two', n)
        break

    nn = i - previously.get(n, i)
    previously[n] = i
    n = nn
