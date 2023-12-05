seeds = []
maps = []
for block in open('2023/05/input.txt').read().split('\n\n'):
    if not seeds:
        seeds = [int(t) for t in block.split(':')[1].split()]
    else:
        map_ = []
        for line in block.splitlines()[1:]:
            dest, src, n = [int(t) for t in line.split()]
            map_.append([src, src+n-1, dest-src])
        maps.append(map_)

#                   mmmmmmmmmmmmmmmmmmm
#           iii          iii              iii
#                 iiIi               iIii
#                  iIiiiiiiiiiiiiiiiiiIi

def apply_map(map_, items):
    result = []
    for item_start, item_end in items:
        for start, end, offset in map_:
            if item_start < start and item_end >= start:
                # overlap at start of map, split!
                items.append((item_start, start-1))
                item_start = start
            if item_start <= end and item_end > end:
                # overlap at end of map, split!
                items.append((end+1, item_end))
                item_end = end

            # now item is either completely inside or outside of the map
            if start <= item_start <= end:
                # found a matching map, apply it and stop processing this item
                item_start += offset
                item_end += offset
                break
        result.append((item_start, item_end))
    return result

items = zip(seeds, seeds)
for map_ in maps:
    items = apply_map(map_, items)
print('one:', min(item[0] for item in items))

items = [(t, t+n-1) for t,n in zip(seeds[::2], seeds[1::2])]
for map_ in maps:
    items = apply_map(map_, items)
print('two:', min(item[0] for item in items))
