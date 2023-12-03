# adding a trailing '.' on every line to ensure no numbers in last column
schematic = [line.strip()+'.' for line in open('2023/03/input.txt')]
width = len(schematic[0])
height = len(schematic)

def options(row, col):
    for y in range(row-1, row+2):
        for x in range(col-1, col+2):
            if 0 <= y < height and 0 <= x < width:
                yield (y, x)

tagged = [[0]*width for _ in range(height)]
gears = []

tag = 1
for row in range(height):
    for col in range(width):
        c = schematic[row][col]
        if c != '.' and not c.isdecimal():
            if c == '*':
                gears.append(tag)
            for y,x in options(row, col):
                if schematic[y][x].isdecimal():
                    tagged[y][x] = tag
            tag += 1

one = 0
twos = {}
for row in range(height):
    number = ''
    tags = set()
    for col in range(width):
        if schematic[row][col].isdecimal():
            number += schematic[row][col]
            tags.add(tagged[row][col])
            continue
        elif number:
            tags.discard(0)
            if tags:
                number = int(number)
                one += number
                for tag in tags:
                    if tag in gears:
                        twos.setdefault(tag, []).append(number)
        number = ''
        tags = set()

print('one:', one)
two = 0
for values in twos.values():
    if len(values) == 2:
        two += values[0] * values[1]
print('two:', two)
