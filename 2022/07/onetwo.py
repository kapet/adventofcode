directories = {}
current_dir = ('/',)
for line in open('input.txt'):
    line = line.strip().split()
    if line[0] == '$':
        if line[1] == 'cd':
            if line[2] == '/':
                current_dir = ('/',)
            elif line[2] == '..':
                current_dir = current_dir[:-1]
            else:
                current_dir = current_dir + (line[2],)
        else:
            assert line[1] == 'ls'
            # all rows that are not commands are ls output anyway
    elif line[0] == 'dir':
        # can ignore directories without files as their size is 0
        pass
    else:
        dir = current_dir
        # add file size to this dir and all parent dirs
        while dir:
            directories[dir] = directories.setdefault(dir, 0) + int(line[0])
            dir = dir[:-1]

print('one:', sum([v for v in directories.values() if v <= 100000]))

fs_size = 70000000
free_space = fs_size - directories[('/',)]
need_to_free = 30000000 - free_space

for v in sorted(directories.values()):
    if v >= need_to_free:
        print('two:', v)
        break
