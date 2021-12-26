#   0123456789a
#  #########################
#  # 0 1 . 2 . 3 . 4 . 5 6 #
#  ##### 7 # 8 # 9 #10 #####
#      #11 #12 #13 #14 #  
#      #15 #16 #17 #18 #  
#      #19 #20 #21 #22 #  
#      #################  

# (row,col)
coordinates = [
    (0,0), (0,1),        (0,3),        (0,5),        (0,7),        (0,9), (0,10),
                  (1,2),        (1,4),        (1,6),        (1,8),
                  (2,2),        (2,4),        (2,6),        (2,8),
                  (3,2),        (3,4),        (3,6),        (3,8),
                  (4,2),        (4,4),        (4,6),        (4,8),
]
coords_to_position = {c:i for i,c in enumerate(coordinates)}

def steps(p0, p1, cache={}):
    # return number of steps between p0 and p1
    key = (p0,p1)
    if key in cache:
        return cache[key]
    c0 = coordinates[p0]
    c1 = coordinates[p1]
    if p0 == p1:
        # if start and destination are same, no steps
        result = 0
    elif c0[1] == c1[1]:
        # within the same column
        result = abs(c1[0]-c0[0])
    else:
        # in different columns, or in the hallway
        # total steps is y dist to hallway plus x dist in hallway
        result = c0[0]+c1[0]+abs(c1[1]-c0[1])
    cache[key] = result
    return result

def check_path(position, p0, p1):
    # return True if nothing blocks the path from p0 to p1
    # p0 itself is not checked, but p1 is checked and if occupied results in False
    assert p0 != p1
    if position[p1] != '.':
        # quick check for destination occupied
        return False
    c0 = coordinates[p0]
    c1 = coordinates[p1]

    if c0[1] == c1[1]:
        # both in same column, just walk the rows
        d = c1[0]-c0[0]
        d = d/abs(d)
        while c0[0] != c1[0]:
            c0 = (c0[0]+d, c0[1])
            if c0 in coords_to_position:
                if position[coords_to_position[c0]] != '.':
                    return False
        return True

    else:
        # currently in different columns, move both to baseline
        # check every position on the way and bail out if occupied
        while c0[0] != 0:
            c0 = (c0[0]-1, c0[1])
            if c0 in coords_to_position:
                if position[coords_to_position[c0]] != '.':
                    return False
        while c1[0] != 0:
            c1 = (c1[0]-1, c1[1])
            if c1 in coords_to_position:
                if position[coords_to_position[c1]] != '.':
                    return False
        # now both on baseline, walk columns until meet
        d = c1[1]-c0[1]
        d = d/abs(d)
        while c0[1] != c1[1]:
            c0 = (c0[0], c0[1]+d)
            if c0 in coords_to_position:
                if position[coords_to_position[c0]] != '.':
                    return False
        return True

def move(position, p0, p1):
    # return updated position string with the amphipod at p0 moved to p1
    amphi = position[p0]
    space = position[p1]
    assert space == '.'
    if p0 < p1:
        return position[:p0]+space+position[p0+1:p1]+amphi+position[p1+1:]
    else:
        return position[:p1]+amphi+position[p1+1:p0]+space+position[p0+1:]
