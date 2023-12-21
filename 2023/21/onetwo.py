garden = [line.strip() for line in open('2023/21/input.txt')]
height = len(garden)
width = len(garden[0])

for starty in range(height):
    if 'S' in garden[starty]:
        startx = garden[starty].index('S')
        break
garden[starty] = garden[starty].replace('S', '.')

# about the input garden:
# - the starting point is in the center
# - there are a few unreachable fields
# - 'walls' can increase length of paths
# - the outside perimeter has no rocks
# - there are free paths from the start to the border
#   => every point on the border is reachable in Manhattan distance length
#   !! this is not the case for the test data!
# - there are diamond shaped diagonals with no rocks
#   => limits every path through the garden to Manhattan distance
#   !! again not in the test data!
# - Manhattan distance means steps expand as a diamond (not a circle!)

def reachable(posy, posx, n_steps):
    distances = {}
    heap = [(posy, posx, 0)]
    while heap:
        posy, posx, steps = heap.pop(0)
        if (posy, posx) in distances:
            continue
        if garden[posy][posx] == '#':
            continue
        distances[(posy, posx)] = steps
        steps += 1
        if steps > n_steps:
            continue
        if posy > 0:
            heap.append((posy-1, posx, steps))
        if posy < height-1:
            heap.append((posy+1, posx, steps))
        if posx > 0:
            heap.append((posy, posx-1, steps))
        if posx < width-1:
            heap.append((posy, posx+1, steps))
    oddeven = n_steps % 2
    return len([i for i in distances.values() if i%2==oddeven])

print('one:', reachable(starty, startx, 64))

# how many fields are reachable with 'unlimited' steps?
total1 = reachable(starty, startx, width+height)

steps = 26501365
# starting point is at 65/65, size is 131/131
# => there are 65 steps from the center to the border
# 26501365-65 => 26501300/131 => 202300
# so that means we create a diamond 202300+1+202300=404601 'gardens' long

# 65 steps to the border means the next garden block has swapped odd/even
total2 = reachable(starty, startx, (width+height)+1)

#                   2
#          1       212
#   2     121     21212
#  212   12121   2121212
#   2     121     21212
#          1       212
#                   2
#
#1: 1      9        9
#2: 4      4       16
#   2      3        4
# element on outside is n^2 with n being the dimension
# element on inside is (n-1)^2
#
# 202300+1 is odd, so 1 blocks make the outside
# => (202300+1)^2 blocks '1' and 202300^2 blocks '2'
two = (202300+1)**2 * total1 + 202300**2 * total2

# 601113655995006 => too high

# missed the corners

#                   2
#         a1b      212
#  a2b   a121b    21212
#  212   12121   2121212
#  c2d   c121d    21212
#         c1d      212
#                   2

# first diamond (n=2)
# a - add bottom right 1
# b - add bottom left 1
# c - add top right 1
# d - add top left 1
# 2t - remove top left 2, remove top right 2
# 2l - remove top left 2, remove bottom left 2
# 2r - remove top right 2, remove bottom right 2
# 2b - remove bottom left 2, remove bottom right 2
# => add one outside diamond 1, remove two outside diamond 2

# second diamond (n=3)
# a - 2* add bottom right 2
# b - 2* add bottom left 2
# c - 2* add top right 2
# d - 2* add top left 2
# 1t - remove top left 1, remove top right 1
# 1tl - remove top left 1
# 1tr - remove top right 1
# 1l - remove top left 1, remove bottom left 1
# 1r - remove top right 1, remove bottom right 1
# 1bl - remove bottom left 1
# 1br - remove bottom right 1
# 1b - remove bottom left 1, remove bottom right 1
# => remove three outside diamond 1, add two outside diamond 2

# => spikes stay the same, for every n (dimension) one more in between per edge
# again 202300+1 is odd, so 1 blocks make the outside
# => remove 202300+1 diamonds '1' and 202300 diamonds '2'

diamond1 = total1 - reachable(starty, startx, 65)
diamond2 = total2 - reachable(starty, startx, 64)

two = two - (202300+1)*diamond1 + 202300*diamond2
print('two:', two)
