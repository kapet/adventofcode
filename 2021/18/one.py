from snailfish import *

# basic testing
n1 = parse('[[[[4,3],4],4],[7,[[8,4],9]]]')
n2 = parse('[1,1]')
n3 = add(n1, n2)
reduce(n3)
assert output(n3) == '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]'

# multi-add testing
data = """[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]"""
values = data.strip().split('\n')
num = parse(values[0])
for line in values[1:]:
    num = add(num, parse(line))
    reduce(num)
assert output(num) == '[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]'

# magnitude testing
assert magnitude(parse('[9,1]')) == 29
assert magnitude(parse('[[9,1],[1,9]]')) == 129
assert magnitude(parse('[[1,2],[[3,4],5]]')) == 143
assert magnitude(parse('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]')) == 1384
assert magnitude(parse('[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]')) == 3488

# example homework
values = open('2021/18/test.txt').readlines()
num = parse(values[0])
for line in values[1:]:
    line = line.strip()
    if not line:
        continue
    num = add(num, parse(line))
    reduce(num)
assert output(num) == '[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]'
assert magnitude(num) == 4140

# actual exercise
values = open('2021/18/input.txt').readlines()
num = parse(values[0])
for line in values[1:]:
    line = line.strip()
    if not line:
        continue
    num = add(num, parse(line))
    reduce(num)
print(output(num))
print(magnitude(num))
