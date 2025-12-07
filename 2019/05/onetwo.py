import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))
import intcode

program = intcode.load('2019/05/input.txt')
out_ = intcode.run(program[:], [1])
print('one', out_[-1])

out_ = intcode.run(program, [5])
print('two', out_[0])
