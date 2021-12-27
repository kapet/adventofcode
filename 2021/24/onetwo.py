import alu

program = []
for line in open('2021/24/input.txt'):
    program.append(line.strip().split())
print('got {} lines of program'.format(len(program)))

# the program is identical for most parts, only three constants differ
var_div = [1, 1, 1, 1, 26, 1, 1, 26, 26, 26, 26, 1, 26, 26]
var_addx = [10, 10, 12, 11, 0, 15, 13, -12, -15, -15, -4, 10, -5, -12]
var_addy = [12, 10, 8, 4, 3, 10, 6, 13, 8, 1, 7, 6, 9, 9]

def alt_step(i, z, data):
    if data == ((z % 26) + var_addx[i]):
        z = z // var_div[i]
    else:
        z = (z // var_div[i]) * 26 + data + var_addy[i]
    return z

def alt_implementation(input_data):
    z = 0
    for i in range(14):
        z = alt_step(i, z, input_data[i])
    return z

if 0:
    # quick test for equivalence
    input_data = [1,3,5,7,9,2,4,6,8,9,9,9,9,9]
    print(alu.ALU(program, input_data))
    print(alt_implementation(input_data))

    input_data = [9,8,7,6,5,4,3,2,1,2,3,4,5,6]
    print(alu.ALU(program, input_data))
    print(alt_implementation(input_data))


# grower,shrinker in pairs
pairs = [(0,13), (1,10), (2,9), (3,4), (5,8), (6,7), (11,12)]

# look for largest solution
solution = [9]*14
for grower,shrinker in sorted(pairs, key=lambda t: t[1]):
    z_values = [0]*15
    for i in range(14):
        z_values[i] = alt_step(i, z_values[i-1], solution[i])

    cmp_value = (z_values[shrinker-1] % 26) + var_addx[shrinker]
    if cmp_value == solution[i]:
        # good match, move on
        continue

    # not a match. have two numbers to tweak:
    # 1. reduce the growth digit if cmp_value is >9
    # 2. reduce the shrink digit if cmp_value is <=9
    # remember that all digits are initialized with a 9
    if cmp_value <= 9:
        solution[shrinker] = cmp_value
    else:
        solution[grower] -= cmp_value - 9

assert alt_implementation(solution) == 0
print('max solution: {}'.format(solution))

# look for smallest solution
solution = [1]*14
for grower,shrinker in sorted(pairs, key=lambda t: t[1]):
    z_values = [0]*15
    for i in range(14):
        z_values[i] = alt_step(i, z_values[i-1], solution[i])

    cmp_value = (z_values[shrinker-1] % 26) + var_addx[shrinker]
    if cmp_value == solution[i]:
        # good match, move on
        continue

    # not a match. have two numbers to tweak:
    # 1. increase the growth digit if cmp_value is <1
    # 2. increase the shrink digit if cmp_value is >=1
    # remember that all digits are initialized with a 1
    if cmp_value >= 1:
        solution[shrinker] = cmp_value
    else:
        solution[grower] += 1 - cmp_value

assert alt_implementation(solution) == 0
print('min solution: {}'.format(solution))
