import re
from itertools import combinations

root = "C:/Users/aiden/Dropbox/git/adventofcode/"
lines = [l.rstrip('\n') for l in open(root + 'day20_input.txt', 'r').readlines()]
flatten = lambda t: [item for sublist in t for item in sublist]

t_lines = open(root + 'day20_input.txt', 'r').read().split("\n\n")

tiles = {}
tile_match = {}
for t in t_lines:
    t = t.split("\n")
    num = re.search("\d+", t[0]).group(0)
    tiles[num] = {'tiles': t[1:len(t)]}
    tile_match[num] = {}


## Process each tile into its sides
max_cols = len(tiles['2311']['tiles'][0])
for t in tiles:
    tmp = tiles[t]['tiles']
    tiles[t]['sides'] = [
        [x for x in tmp[0]], ## Top
        [x[(max_cols - 1)] for x in tmp], ## Left
        [x[0] for x in tmp], ## Right
        [x for x in tmp[(len(tmp) - 1)]] ## Bottom
    ]

def check_sides(x1, x2):
    if x1 == x2:
        return True
    elif x1[::-1] == x2:
        return True
    elif x1 == x2[::-1]:
        return True
    elif x1[::-1] == x2[::-1]:
        return True
    else:
        return False


corners = []
for k in tiles:
    t = tiles[k]
    n_match = 0
    to_search = [x for x in tiles.keys() if x != k]
    for k2 in to_search:## Search every other tile
        t2 = tiles[k2]
        ## Search each tile to check, check each side
        for t_side in range(0,4):
            if t_side not in tile_match[k]:            
                for t2_side in range(0,4):
                    res = check_sides(t['sides'][t_side], t2['sides'][t2_side])
                    if res:
                        tile_match[k][t_side] =  {k2: t2_side}
                        tile_match[k2][t2_side] = {k: t_side}

## Find tiles that only have 2 matches
ans = 1
for k in tile_match:
    if len(tile_match[k]) == 2:
        print(k)
        ans *= int(k)