import unittest

import alu

def parse(progstr):
    program = []
    for l in progstr.split('\n'):
        program.append(l.strip().split())
    return program


class TestALU(unittest.TestCase):
    def test_example1(self):
        program = parse('''inp x
                           mul x -1''')

        result = alu.ALU(program, [3])
        self.assertEqual(result['x'], -3)

        result = alu.ALU(program, [-1])
        self.assertEqual(result['x'], 1)

    def test_example2(self):
        program = parse('''inp z
                           inp x
                           mul z 3
                           eql z x''')

        result = alu.ALU(program, [1, 3])
        self.assertEqual(result['z'], 1)

        result = alu.ALU(program, [1, 4])
        self.assertEqual(result['z'], 0)

    def test_example3(self):
        program = parse('''inp w
                           add z w
                           mod z 2
                           div w 2
                           add y w
                           mod y 2
                           div w 2
                           add x w
                           mod x 2
                           div w 2
                           mod w 2''')

        result = alu.ALU(program, [11])
        self.assertEqual(result['z'], 1)
        self.assertEqual(result['y'], 1)
        self.assertEqual(result['x'], 0)
        self.assertEqual(result['w'], 1)

        result = alu.ALU(program, [4])
        self.assertEqual(result['z'], 0)
        self.assertEqual(result['y'], 0)
        self.assertEqual(result['x'], 1)
        self.assertEqual(result['w'], 0)


if __name__ == '__main__':
    unittest.main()