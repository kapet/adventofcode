import unittest

import onetwo


class TestReverse(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(0, onetwo._reverse(0))

    def test_allset(self):
        self.assertEqual(1023, onetwo._reverse(1023))

    def test_reversable(self):
        for val in (1, 47, 255, 1000):
            self.assertEqual(val, onetwo._reverse(onetwo._reverse(val)))


class TestRotate(unittest.TestCase):
    def test_order(self):
        v0, v1, v2, v3 = 0, 48, 72, 132  # symmetric in 10 bit!
        self.assertEqual([v3, v0, v1, v2], onetwo._rotate([v0, v1, v2, v3]))

    def test_reversing(self):
        self.assertEqual([512, 1, 512, 1], onetwo._rotate([1, 1, 1, 1]))

    def test_allaround(self):
        v = [1,2,3,4]
        t = onetwo._rotate(v)
        t = onetwo._rotate(t)
        t = onetwo._rotate(t)
        t = onetwo._rotate(t)
        self.assertEqual(v, t)


class TestFlip(unittest.TestCase):
    def test_order(self):
        v0, v1, v2, v3 = 0, 48, 72, 132  # symmetric in 10 bit!
        self.assertEqual([v1, v0, v3, v2], onetwo._flip([v0, v1, v2, v3]))

    def test_reversing(self):
        self.assertEqual([512, 512, 512, 512], onetwo._flip([1, 1, 1, 1]))

    def test_backandforth(self):
        v = [1,2,3,4]
        t = onetwo._flip(v)
        t = onetwo._flip(t)
        self.assertEqual(v, t)


class TestBitModification(unittest.TestCase):
    def test_rotate(self):
        data = [[1, 2], [3, 4]]
        self.assertEqual([[3, 1], [4, 2]], onetwo.bits_rotate_cw(data))
        self.assertEqual([[2, 4], [1, 3]], onetwo.bits_rotate_ccw(data))
        self.assertEqual(data, onetwo.bits_rotate_cw(onetwo.bits_rotate_ccw(data)))

    def test_flip(self):
        data = [[1, 2], [3, 4]]
        self.assertEqual([[2, 1], [4, 3]], onetwo.bits_flip_h(data))
        self.assertEqual([[3, 4], [1, 2]], onetwo.bits_flip_v(data))
        self.assertEqual(data, onetwo.bits_flip_h(onetwo.bits_flip_h(data)))
        self.assertEqual(data, onetwo.bits_flip_v(onetwo.bits_flip_v(data)))

    def test_and(self):
        self.assertEqual(['##'], onetwo.bits_and(['##'], ['##']))
        self.assertEqual([' #'], onetwo.bits_and(['##'], ['.#']))
        self.assertEqual(['# '], onetwo.bits_and(['#.'], ['##']))
        self.assertEqual(['  '], onetwo.bits_and(['#.'], ['.#']))

        self.assertEqual(['# ', ' #'], onetwo.bits_and(
            ['#.', '.#'], ['##', '##']))


if __name__ == '__main__':
    unittest.main()