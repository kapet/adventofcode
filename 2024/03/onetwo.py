import re

data = open('2024/03/input.txt').read()

one = two = 0
do = True
for element in re.finditer(r'mul\((\d+),(\d+)\)|(don\'t)|(do)', data):
    match element.groups():
        case (_, _, "don't", _):
            do = False
        case (_, _, _, "do"):
            do = True
        case (x, y, _, _):
            xy = int(x) * int(y)
            one += xy
            if do:
                two += xy

print('one:', one)
print('two:', two)