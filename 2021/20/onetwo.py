with open('2021/20/input.txt') as f:
    algo = f.readline().strip()
    assert f.readline().strip() == ''
    data = [l.strip() for l in f]

algo = [t=='#' and 1 or 0 for t in algo]

width = len(data[0])
height = len(data) 
newdata = []
for row in data:
    newdata.append([t=='#' and 1 or 0 for t in row])
data = newdata

print('got {} bits algo and image {}x{}'.format(len(algo), width, height))

# we start with all pixels outside of the input image as unset
offworld = 0

def add_border():
    global width, height, data

    newwidth = width + 4
    newheight = height + 4
    newdata = [[offworld]*newwidth for _ in range(newheight)]
    for i in range(height):
        for j in range(width):
            newdata[2+i][2+j] = data[i][j]

    data = newdata
    width = newwidth
    height = newheight

def crop():
    global width, height, data

    while all(t==offworld for t in data[0]):
        del data[0]
        height -= 1
    while all(t==offworld for t in data[-1]):
        del data[-1]
        height -= 1
    while all(t[0]==offworld for t in data):
        data = [t[1:] for t in data]
        width -= 1
    while all(t[-1]==offworld for t in data):
        data = [t[:-1] for t in data]
        width -= 1

def enhance():
    # expects that add_border was run
    global data, offworld

    # calc new offworld
    if offworld == 0:
        offworld = algo[0]
    else:
        offworld = algo[511]

    newdata = [[offworld]*width for _ in range(height)]
    for i in range(1, height-1):
        for j in range(1, width-1):
            val = 0
            for bit in data[i-1][j-1:j+2] + data[i][j-1:j+2] + data[i+1][j-1:j+2]:
                val = (val<<1)|bit
            val = algo[val]
            newdata[i][j] = val
    
    data = newdata

for iteration in range(1, 51):
    add_border()
    enhance()
    crop()
    print('total pixels after {} enhancements: {}'.format(iteration, sum(sum(l) for l in data)))

if 0:
    for line in data:
        print(''.join(t and '#' or ' ' for t in line))