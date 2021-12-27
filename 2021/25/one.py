import array
import time

data = [l.strip() for l in open('2021/25/input.txt', 'rb')]
height = len(data)
width = len(data[0])

seafloor = array.array('B')
for row in data:
    seafloor.frombytes(row)

def print_floor():
    for y in range(height):
        p = y*width
        line = seafloor[p:p+width]
        print(line.tobytes().decode('ascii'))

print('initial state:')
print_floor()

t = 0
i = 0
while True:
    i += 1

    changed = False
    for herd in (ord(b'>'), ord(b'v')):
        newfloor = array.array('B', seafloor)
        for y in range(height):
            for x in range(width):
                if seafloor[y*width+x] == herd:
                    nx,ny = x,y
                    if herd == ord(b'>'):
                        nx += 1
                        if nx >= width:
                            nx = 0
                    else:
                        ny += 1
                        if ny >= height:
                            ny = 0
                    if seafloor[ny*width+nx] == ord('.'):
                        newfloor[ny*width+nx] = herd
                        newfloor[y*width+x] = ord('.')
        if seafloor != newfloor:
            changed = True
        seafloor = newfloor

    tn = time.time()
    if tn-t > 1:
        t = tn
        print('\nafter {} steps:'.format(i))
        print_floor()

    if not changed:
        break

print('\nfinal state:')
print_floor()
print('stable after {} steps'.format(i))