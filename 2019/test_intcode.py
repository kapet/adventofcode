import tempfile
import unittest

import intcode


class TestLoad(unittest.TestCase):
    def test_load(self):
        with tempfile.NamedTemporaryFile(delete_on_close=False) as tmp:
            tmp.write(b'1,2,3,4,5,6\n')
            tmp.flush()

            result = intcode.load(tmp.name)
            self.assertSequenceEqual([1,2,3,4,5,6], result)


class TestRun(unittest.TestCase):
    def test_add_pos(self):
        # [7] = [5] + [6]
        #         0  1  2  3   4  5  6  7
        prog   = [1, 5, 6, 7, 99, 4, 5, 0]
        expect = [1, 5, 6, 7, 99, 4, 5, 9] 
        out = intcode.run(prog)
        self.assertSequenceEqual(expect, prog)
        self.assertEqual([], out)

    def test_add_imm(self):
        # [5] = 2 * 3
        #            0  1  2  3   4  5
        prog   = [1101, 2, 3, 5, 99, 0]
        expect = [1101, 2, 3, 5, 99, 5] 
        out = intcode.run(prog)
        self.assertSequenceEqual(expect, prog)
        self.assertEqual([], out)

    def test_mul_pos(self):
        # [7] = [5] * [6]
        #         0  1  2  3   4  5  6  7
        prog   = [2, 5, 6, 7, 99, 4, 5, 0]
        expect = [2, 5, 6, 7, 99, 4, 5, 20] 
        out = intcode.run(prog)
        self.assertSequenceEqual(expect, prog)
        self.assertEqual([], out)

    def test_mul_imm(self):
        # [5] = [5] * 3
        #            0  1  2  3   4   5
        prog   = [1002, 5, 3, 5, 99, 33]
        expect = [1002, 5, 3, 5, 99, 99] 
        out = intcode.run(prog)
        self.assertSequenceEqual(expect, prog)
        self.assertEqual([], out)

    def test_input(self):
        # in -> [3]
        #         0  1   2   3
        prog   = [3, 3, 99, 12]
        expect = [3, 3, 99, 23]
        out = intcode.run(prog, input_=[23])
        self.assertSequenceEqual(expect, prog)
        self.assertEqual([], out)

    def test_output_pos(self):
        # [3] -> out 
        #         0  1   2   3
        prog   = [4, 3, 99, 12]
        expect = [4, 3, 99, 12]
        out = intcode.run(prog)
        self.assertSequenceEqual(expect, prog)
        self.assertEqual([12], out)

    def test_output_imm(self):
        # 42 -> out 
        #           0   1   2
        prog   = [104, 42, 99]
        expect = [104, 42, 99]
        out = intcode.run(prog)
        self.assertSequenceEqual(expect, prog)
        self.assertEqual([42], out)

    def test_comp_eq_pos(self):
        prog = [3,9,8,9,10,9,4,9,99,-1,8]
        self.assertEqual([0], intcode.run(prog, [7]))
        self.assertEqual([1], intcode.run(prog, [8]))
        self.assertEqual([0], intcode.run(prog, [9]))

    def test_comp_lt_pos(self):
        prog = [3,9,7,9,10,9,4,9,99,-1,8]
        self.assertEqual([1], intcode.run(prog, [7]))
        self.assertEqual([0], intcode.run(prog, [8]))
        self.assertEqual([0], intcode.run(prog, [9]))

    def test_comp_eq_imm(self):
        prog = [3,3,1108,-1,8,3,4,3,99]
        self.assertEqual([0], intcode.run(prog, [7]))
        self.assertEqual([1], intcode.run(prog, [8]))
        self.assertEqual([0], intcode.run(prog, [9]))

    def test_comp_lt_pos(self):
        prog = [3,3,1107,-1,8,3,4,3,99]
        self.assertEqual([1], intcode.run(prog, [7]))
        self.assertEqual([0], intcode.run(prog, [8]))
        self.assertEqual([0], intcode.run(prog, [9]))

    def test_jump_pos(self):
        prog = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
        self.assertEqual([0], intcode.run(prog, [0]))
        self.assertEqual([1], intcode.run(prog, [42]))

    def test_jump_imm(self):
        prog = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
        self.assertEqual([1], intcode.run(prog, [42]))
        self.assertEqual([0], intcode.run(prog, [0]))

if __name__ == '__main__':
    unittest.main()