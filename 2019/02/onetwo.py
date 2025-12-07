import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))
import intcode

original_program = intcode.load('2019/02/input.txt')

def run(noun, verb):
    program = original_program[:]
    program[1] = noun
    program[2] = verb
    intcode.run(program)
    return program[0]

print('one', run(12, 2))
for noun in range(99):
    for verb in range(99):
        result = run(noun, verb)
        if result == 19690720:
            print('two', 100*noun + verb)
            sys.exit()
