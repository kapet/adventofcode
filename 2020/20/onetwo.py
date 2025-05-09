import math

# tiles are 10x10
# test is 9 tiles (3x3), input is 144 tiles (12x12)
# 10 bits -> 1024 combinations
# 144 tiles * 4 sides * 2 directions -> 1152 combinations
# 12x12 -> 4*12 = 48 outside edges and 2*11*12 = 264 inside edges
# 264+48=312 is much lower than 1024, so an unambiguous set is possible
# assumption: input problem is unambigous, i.e. no edge-code appears more than twice

def _edge(line):
    # parse a line of '.' and '#' into a number
    return int(''.join(line).replace('.', '0').replace('#', '1'), 2)

def _reverse(val, n=10):
    # reverse the bits of a number with n bits
    return int(''.join(list(reversed(bin(val)[2:]))).ljust(n, '0'), 2)

def _rotate(vals):
    # rotate a list of edges clockwise
    return [
        _reverse(vals[3]),
        vals[0],
        _reverse(vals[1]),
        vals[2]
    ]

def _flip(vals):
    # mirror a list of edges diagonally (so it lands on its "back")
    return [
        _reverse(vals[1]),
        _reverse(vals[0]),
        _reverse(vals[3]),
        _reverse(vals[2])
    ]

def bits_rotate_cw(data):
    return [list(t) for t in zip(*data[::-1])]

def bits_rotate_ccw(data):
    return [list(t) for t in reversed(list(zip(*data)))]

def bits_flip_h(data):
    return [list(reversed(l)) for l in data]

def bits_flip_v(data):
    return list(reversed(data))

def bits_and(data1, data2):
    assert len(data1) == len(data2)
    assert len(data1[0]) == len(data2[0])
    result = []
    for y in range(len(data1)):
        line = []
        for x in range(len(data1[y])):
            if data1[y][x] == data2[y][x] == '#':
                line.append('#')
            else:
                line.append(' ')
        result.append(''.join(line))
    return result


class Tile:
    def __init__(self, nr, bits):
        self.nr = nr
        self.bits = bits

        # original edges
        edges = self._edges()
        # diagonally flipped over / mirrored in both axises
        reversed = _flip(edges)
        self.all_edgecodes = edges + reversed
        # add all rotations of "front side"
        self.edges = [edges]
        for _ in range(3):
            self.edges.append(_rotate(self.edges[-1]))
        assert _rotate(self.edges[-1]) == edges
        # add all rotations of "back side"
        self.edges.append(reversed)
        for _ in range(3):
            self.edges.append(_rotate(self.edges[-1]))
        assert _rotate(self.edges[-1]) == reversed

        # use the original orientation for now
        # 0..3 is rotations of front, 4..7 is of the back (mirrored)
        self.orientation = 0

    def __repr__(self):
        return f'[{self.nr}@{self.orientation}]'

    def _edges(self):
        # parse the edges of a specific tile
        # returns (top, right, bottom, left)
        # direction is always MSB top/left to LSB bottom/right
        # -> if two tiles match then one's right == the other's left, etc
        return [
            _edge(self.bits[0]),
            _edge(l[-1] for l in self.bits),
            _edge(self.bits[-1]),
            _edge(l[0] for l in self.bits),
        ]
    
    def top(self):
        return self.edges[self.orientation][0]

    def right(self):
        return self.edges[self.orientation][1]

    def bottom(self):
        return self.edges[self.orientation][2]

    def left(self):
        return self.edges[self.orientation][3]
    
    def export(self):
        # the border is dropped
        data = [l[1:-1] for l in self.bits[1:-1]]
        o = self.orientation
        if o >= 4:
            # to match the result of _flip
            data = bits_flip_v(data)
            data = bits_rotate_ccw(data)
            o -= 4
        while o > 0:
            data = bits_rotate_cw(data)
            o -= 1
        assert len(data) == 8
        assert len(data[0]) == 8
        return data


if __name__ == '__main__':
    tiles = {}
    for rawtile in open('2020/20/input.txt').read().split('\n\n'):
        lines = rawtile.strip().split('\n')
        nr = int(lines[0].split()[1][:-1])
        tiles[nr] = Tile(nr, [list(l) for l in lines[1:]])

    # index edge code -> tile nr
    edge_codes = {}
    for tile in tiles.values():
        for e in tile.all_edgecodes:
            edge_codes.setdefault(e, set()).add(tile.nr)

    # find tiles with unique edges, these are corners and outside edges
    # only need to check original orientation, duplicates will match across
    # rotations and mirroring
    corners = []
    outsides = []
    for tile in tiles.values():
        unique = 0
        for e in tile.edges[0]:
            if len(edge_codes[e]) == 1:
                unique += 1
        if unique == 1:
            outsides.append(tile.nr)
        elif unique == 2:
            corners.append(tile.nr)
        else:
            assert unique == 0

    # Fun fact: for part 1 we only need to know the numbers of the corner tiles...
    assert len(corners) == 4
    print('one', math.prod(corners))

    # assemble the picture
    sidelen = math.isqrt(len(tiles))
    solution = [[None] * sidelen for _ in range(sidelen)]

    # pick a random corner tile and rotate it correctly
    t = solution[0][0] = tiles[corners[0]]
    while len(edge_codes[t.top()]) + len(edge_codes[t.left()]) != 2:
        t.orientation += 1

    # first row
    for x in range(1, sidelen):
        c = solution[0][x-1].right()
        t = set(edge_codes[c]) - set([solution[0][x-1].nr])
        assert len(t) == 1
        t = t.pop()
        t = solution[0][x] = tiles[t]
        while len(edge_codes[t.top()]) != 1 or t.left() != c:
            t.orientation += 1

    # now just fill in all other tiles, assuming edges to be unique
    for y in range(1, sidelen):
        # first tile in row
        c = solution[y-1][0].bottom()
        t = set(edge_codes[c]) - set([solution[y-1][0].nr])
        assert len(t) == 1
        t = t.pop()
        t = solution[y][0] = tiles[t]
        while len(edge_codes[t.left()]) != 1 or t.top() != c:
            t.orientation += 1
            assert t.orientation <= 7

        for x in range(1, sidelen):
            ct = solution[y-1][x].bottom()
            cl = solution[y][x-1].right()
            t = set(edge_codes[ct]) - set([solution[y-1][x].nr])
            assert len(t) == 1
            t = t.pop()
            t = solution[y][x] = tiles[t]
            while t.top() != ct or t.left() != cl:
                t.orientation += 1
                assert t.orientation <= 7

    # assemble the actual image
    image = []
    for row in solution:
        tiles = [t.export() for t in row]
        for r in range(8):
            data = ''.join(''.join(t[r]) for t in tiles)
            image.append(data)

    # look for sea monsters
    monster = [
        '                  # ',
        '#    ##    ##    ###',
        ' #  #  #  #  #  #   ',
    ]
    wh = sidelen * 8
    for orientation in range(8):
        found = 0
        for y in range(wh-3+1):
            for x in range(wh-20+1):
                data = [
                    image[y][x:x+20],
                    image[y+1][x:x+20],
                    image[y+2][x:x+20],
                ]
                if monster == bits_and(data, monster):
                    found += 1

        if found:
            two = sum(l.count('#') for l in image)
            two -= found * sum(l.count('#') for l in monster)
            print('two', two)
            break

        image = bits_rotate_cw(image)
        if orientation == 3:
            image = bits_flip_h(image)
