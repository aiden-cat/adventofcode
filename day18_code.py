import re
from itertools import combinations

root = "C:/Users/aiden/Dropbox/git/adventofcode/"
lines = [l.rstrip('\n') for l in open(root + 'day18_input.txt', 'r').readlines()]
flatten = lambda t: [item for sublist in t for item in sublist]

line = "9 * (3 + 9 + 5 + 7) * 5 + 6"
line = line.replace(' ', '')

nums = [str(x) for x in list(range(10))]
def calc(line):
    for i in range(len(line)):
        if line[i] in nums and i == 0:
            ans = int(line[i])
        elif line[i] in nums and line[i+1] == '*':
            ans * 


lines2 = [re.sub(r"(\d+)", r"I(\1)", l).replace("*", "-") for l in lines]

WTF this genius solution https://github.com/axieax/advent-of-code-2020/blob/main/day18/p1.py

https://gist.github.com/andreypopp/f789114ab45c101f901ea1b0444acd8c

https://github.com/viliampucik/adventofcode/blob/master/2020/18.py