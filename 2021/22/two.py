import collections
import re

Cuboid = collections.namedtuple('Cuboid', ['minx', 'maxx', 'miny', 'maxy', 'minz', 'maxz'])

steps = []
parser_re = re.compile(r'([onf]*) x=(-?\d*)\.\.(-?\d*),y=(-?\d*)\.\.(-?\d*),z=(-?\d*)\.\.(-?\d*)')
for line in open('2021/22/input.txt'):
    match = parser_re.fullmatch(line.strip())
    groups = list(match.groups())
    state = groups[0] == 'on'
    cube = Cuboid(*(int(t) for t in groups[1:]))
    # expect max values always higher than min ones
    assert cube.maxx >= cube.minx
    assert cube.maxy >= cube.miny
    assert cube.maxz >= cube.minz
    steps.append((state, cube))

print('loaded {} steps'.format(len(steps)))

# brute force iteration is way too slow
# idea: intersect cuboids, build a stack of non-overlapping ones for 'on'
# start with the first step, then add steps, always testing against whole stack
# if intersect: break older cuboid into sub-cuboids, throw the intersecting one away
# if 'on': keep new cuboid, if 'off' throw new cuboid away after no more intersections (default is off anyway)
# when done sum size of each cuboid in stack

def cube_split(cube, splitter):
    # cut cube into up to 26 new cubes, all around the splitter cube
    # the splitter cube is NOT included in the result
    # this basically cuts the splitter out of cube and returns the rest
    xpairs = [(cube.minx, splitter.minx-1), (splitter.minx, splitter.maxx), (splitter.maxx+1, cube.maxx)]
    ypairs = [(cube.miny, splitter.miny-1), (splitter.miny, splitter.maxy), (splitter.maxy+1, cube.maxy)]
    zpairs = [(cube.minz, splitter.minz-1), (splitter.minz, splitter.maxz), (splitter.maxz+1, cube.maxz)]

    result = []
    for minx,maxx in xpairs:
        if maxx-minx < 0:
            continue
        for miny,maxy in ypairs:
            if maxy-miny < 0:
                continue
            for minz,maxz in zpairs:
                if maxz-minz < 0:
                    continue
                subcube = Cuboid(minx, maxx, miny, maxy, minz, maxz)
                if subcube != splitter:
                    result.append(subcube)
    return result

def cube_intersect(cube1, cube2):
    # intersects cube1 and cube2
    # returns [[cubes only in cube1], intersecting cube if any, [cubes only in cube2]]
    icube = Cuboid(
        minx=max(cube1.minx, cube2.minx), maxx=min(cube1.maxx, cube2.maxx),
        miny=max(cube1.miny, cube2.miny), maxy=min(cube1.maxy, cube2.maxy),
        minz=max(cube1.minz, cube2.minz), maxz=min(cube1.maxz, cube2.maxz))
    
    xdiff = icube.maxx - icube.minx
    ydiff = icube.maxy - icube.miny
    zdiff = icube.maxz - icube.minz

    if xdiff >= 0 and ydiff >= 0 and zdiff >= 0:
        # they intersect
        return [cube_split(cube1, icube), icube, cube_split(cube2, icube)]
    else:
        # no intersection
        return [[cube1], None, [cube2]]

assert steps[0][0] == True
stack = [steps[0][1]]  # just the cuboid

# iterate through all steps
for target_state, cube in steps[1:]:
    newstack = []

    # check all existing cubes against new one
    for existing_cube in stack:
        lcubes, icube, _ = cube_intersect(existing_cube, cube)
        if icube:
            # all lcubes are completely unaffected
            newstack.extend(lcubes)
            # icube and rcubes are part of the new cube, they will be added later
        else:
            # new cube does not intersect with old one, can just keep the old one
            newstack.append(existing_cube)

    # whole stack has been checked, now add the new step if 'on'
    if target_state:
        newstack.append(cube)

    stack = newstack

total50 = 0
total = 0
for cube in stack:
    _, icube, _ = cube_intersect(cube, Cuboid(-50,50,-50,50,-50,50))
    if icube:
        total50 += (icube.maxx-icube.minx+1)*(icube.maxy-icube.miny+1)*(icube.maxz-icube.minz+1)
    total += (cube.maxx-cube.minx+1)*(cube.maxy-cube.miny+1)*(cube.maxz-cube.minz+1)
print('total on in -50..50: {}'.format(total50))
print('total on overall: {}'.format(total))
