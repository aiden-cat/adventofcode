import re
from itertools import combinations

root = "C:/Users/aiden/Dropbox/git/adventofcode/"
lines = [l.rstrip('\n') for l in open(root + 'day14_input.txt', 'r').readlines()]
flatten = lambda t: [item for sublist in t for item in sublist]

## Input today is only one line
day15_inp = [16,11,15,0,1,7]

inp = [0,3,6]
inp = [3,1,2]
said = {}
for i in range(30000000):
    # print(i)
    if inp != []:
        to_say = inp.pop(0)
        said[to_say] = [i + 1]
    else:
        if to_say in said.keys():
            if len(said[to_say]) == 1:
                to_say = 0
            else:
                to_say = said[to_say][-1] - said[to_say][-2]
        if to_say in said.keys():
            said[to_say].append(i+1)
        else:
            said[to_say] = [i+1]

## Change range to 2000 and re-run for prat 1...
print(to_say)