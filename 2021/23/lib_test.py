import unittest

import lib


class TestSteps(unittest.TestCase):
    def test_cache(self):
        cache = {}
        _ = lib.steps(0,0, cache=cache)
        _ = lib.steps(0,1, cache=cache)
        _ = lib.steps(3,4, cache=cache)
        self.assertEqual(cache, {(0,0):0, (0,1):1, (3,4):2})

    def test_same_position(self):
        self.assertEqual(lib.steps(0,0), 0)

    def test_same_column(self):
        self.assertEqual(lib.steps(7, 11), 1)
        self.assertEqual(lib.steps(14, 10), 1)

    def test_both_hallway(self):
        self.assertEqual(lib.steps(0, 3), 5)
        self.assertEqual(lib.steps(6, 4), 3)

    def test_one_column(self):
        self.assertEqual(lib.steps(0, 7), 3)
        self.assertEqual(lib.steps(12, 1), 5)

    def test_different_columns(self):
        self.assertEqual(lib.steps(7, 9), 6)
        self.assertEqual(lib.steps(14, 9), 5)

        self.assertEqual(lib.steps(19, 20), 10)
        self.assertEqual(lib.steps(17, 12), 7)


class TestCheckPath(unittest.TestCase):
    def test_self_target_fails(self):
        with self.assertRaises(Exception):
            _ = lib.check_path('', 0, 0)

    def test_target_occupied(self):
        #      0123456789abcde
        pos = '.A.....A.......'
        self.assertFalse(lib.check_path(pos, 1, 7))
        self.assertFalse(lib.check_path(pos, 2, 7))

    def test_same_column(self):
        #      0123456789abcde
        pos = '.......ABC.ABCD'
        self.assertTrue(lib.check_path(pos, 14, 10)) # D moves one up
        self.assertFalse(lib.check_path(pos, 8, 12)) # upper B tries moving down

    def test_both_hallway(self):
        #      0123456789abcde
        pos = '.A...B.........'
        self.assertTrue(lib.check_path(pos, 5, 2)) # B stays right of A
        self.assertFalse(lib.check_path(pos, 1, 6)) # A runs into B

    def test_different_columns(self):
        #      0123456789abcde
        pos = '.C.....A.....B.'
        self.assertTrue(lib.check_path(pos, 7, 14)) # A moves into empty column
        self.assertFalse(lib.check_path(pos, 13, 0)) # B runs into C in hallway
        self.assertFalse(lib.check_path(pos, 1, 11)) # C runs into A in room
        self.assertTrue(lib.check_path(pos, 1, 9)) # C moves next to B
        self.assertTrue(lib.check_path(pos, 7, 9)) # A moves next to B

        #      0123456ABCDabcdABCDabcd
        pos = '................B..A...'
        self.assertTrue(lib.check_path(pos, 16, 15)) # B moves next to A
        self.assertFalse(lib.check_path(pos, 19, 20)) # A runs into B


class TestMove(unittest.TestCase):
    def test_forward(self):
        self.assertEqual(lib.move('A-------------.', 0, 14), '.-------------A')
        self.assertEqual(lib.move('-A-----------.-', 1, 13), '-.-----------A-')
        self.assertEqual(lib.move('-----A.--------', 5,  6), '-----.A--------')
        self.assertEqual(lib.move('A---------------------.', 0, 22), '.---------------------A')

    def test_backward(self):
        self.assertEqual(lib.move('.-------------B', 14, 0), 'B-------------.')
        self.assertEqual(lib.move('-.-----------B-', 13, 1), '-B-----------.-')
        self.assertEqual(lib.move('-----.B--------',  6, 5), '-----B.--------')
        self.assertEqual(lib.move('.---------------------B', 22, 0), 'B---------------------.')

    def test_donotdisturb(self):
        self.assertEqual(lib.move('A0123456789abc.', 0, 14), '.0123456789abcA')
        self.assertEqual(lib.move('0.123456789abBc', 13, 1), '0B123456789ab.c')
        self.assertEqual(lib.move('abcdefghiAk.mnopqrstuvw', 9, 11), 'abcdefghi.kAmnopqrstuvw')


if __name__ == '__main__':
    unittest.main()
