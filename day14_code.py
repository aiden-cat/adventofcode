import re
from itertools import combinations

root = "C:/Users/aiden/Dropbox/git/adventofcode/"
lines = [l.rstrip('\n') for l in open(root + 'day14_input.txt', 'r').readlines()]
flatten = lambda t: [item for sublist in t for item in sublist]

ids = {}
for line in lines:
    if 'mask' in line:
        mask = re.search("(?<== ).*", line).group(0)
        mask = [s for s in mask]
    else:
        idx = re.search("(?<=\[).*(?=\])", line).group(0)
        num = re.search("(?<== ).*", line).group(0)
        bits = '{0:036b}'.format(int(num))
        bits = [b for b in bits]
        num2 = bits.copy()
        for i in range(len(mask)):
            if mask[i] in ['1', '0']:
                num2[i] = mask[i]
        ids[idx] = num2


ans = 0
for id in ids.keys():
    ans += int(''.join(ids[id]), 2)


print(ans)

## Part 2
ids = {}
combs = {}
for line in lines:
    if 'mask' in line:
        mask = re.search("(?<== ).*", line).group(0)
        mask = [s for s in mask]
    else:
        idx = re.search("(?<=\[).*(?=\])", line).group(0)
        num = re.search("(?<== ).*", line).group(0)
        bits = '{0:036b}'.format(int(num))
        bits = [b for b in bits]
        num2 = bits.copy()
        for i in range(len(mask)):
            if mask[i] in ['1', 'X']:
                num2[i] = mask[i]
        num_x = len([x for x in num2 if x == 'X'])
        if num_x not in combs.keys():
            comb = set(list(combinations([0,1]*num_x*2, num_x)))
            combs[num_x] = comb
        else:
            comb = combs[num_x]
        for c in list(comb):
            c = list(c)
            tmp = [x if x != 'X' else str(c.pop(0)) for x in num2]
            ids[int(''.join(tmp),2)] = num

ans = 0
for id in ids.keys():
    ans += int(ids[id])