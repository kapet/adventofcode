import collections

maze = [line.strip() for line in open('2023/23/test.txt')]
height = len(maze)
width = len(maze[0])

starty, startx = 0, 1
endy, endx = height-1, width-2
assert maze[starty][startx] == maze[endy][endx] == '.'

def longest_path(possible_steps):
    visited_root = collections.ChainMap()
    max_distances = [[-1]*width for _ in range(height)]
    heap = []
    
    heap.append((1, starty+1, startx, visited_root))
    visited_root[(starty, startx)] = True
    max_distances[starty][startx] = 0

    while heap:
        print('####', len(heap))
        # pop from the end -> DFS, priority to high number of steps
        steps, posy, posx, visited = heap.pop() 
        while True:
            if max_distances[posy][posx] >= steps:
                # have previously seen a better/longer path!
                print('  STOP: cheap', steps, max_distances[posy][posx])
                break
            visited[(posy, posx)] = True
            max_distances[posy][posx] = steps
            if (posy, posx) == (endy, endx):
                print('   STOP: end', steps)
                break
            if 1:
                for y, line in enumerate(maze):
                    out = []
                    for x, c in enumerate(line):
                        if (y,x) == (posy, posx):
                            c = 'X'
                        elif (y,x) in visited:
                            c = 'o'
                        out.append(c)
                    print('          ' + ''.join(out))
                print()
            next_steps = []
            current_field = maze[posy][posx]
            for incy, incx, ok in possible_steps:
                if current_field in ok:
                    newy = posy+incy
                    newx = posx+incx
                    if maze[newy][newx] in ok and (newy, newx) not in visited:
                        next_steps.append((newy, newx))
            if not next_steps:
                print('   STOP: stuck')
                break
            steps += 1
            if len(next_steps) > 1:
                for newy, newx in next_steps[1:]:
                    heap.append((steps, newy, newx, visited.new_child()))
                    visited = visited.new_child()
            posy, posx = next_steps[0]
    return max_distances[endy][endx]

#print('one:', longest_path([(0,1,'.>'), (0,-1,'.<'), (1,0,'.v'), (-1,0,'.^')]))
print('two:', longest_path([(0,1,'.><v^'), (0,-1,'.><v^'), (1,0,'.><v^'), (-1,0,'.><v^')]))

# not: 5006, too low

if 0:
    for line in maze:
        print(line)
