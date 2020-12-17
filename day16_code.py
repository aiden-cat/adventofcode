import re
from itertools import combinations

root = "C:/Users/aiden/Dropbox/git/adventofcode/"
lines = [l.rstrip('\n') for l in open(root + 'day16_input.txt', 'r').readlines()]
flatten = lambda t: [item for sublist in t for item in sublist]

valid = {}
valid_nums = []
for i in range(20):
    d = lines[i].split(":")[0]
    nums = re.findall("\d+", lines[i].split(":")[1])
    nums = [int(n) for n in nums]
    nums = list(range(nums[0], nums[1] + 1)) + list(range(nums[2], nums[3] + 1)) 
    valid[d] = nums
    valid_nums.append(nums)

valid_nums = flatten(valid_nums)
valid_nums = [int(n) for n in valid_nums]
err = 0

valid_ticket = []
for line in lines[25:267]:
    tmp = [int(n) for n in line.split(",") if int(n) not in valid_nums]
    if len(tmp)< 1:
        valid_ticket.append(line)
    err += sum(tmp)

## Determine order
valid_ticket = [v.split(",") for v in valid_ticket]
tick_ord = {}
orig_ord = list(valid.keys())
for o in orig_ord:
    tick_ord[o] = {}
    for idx in range(len(valid_ticket[0])):
        tick_ord[o][idx] = 0


for w in orig_ord:
    for tick in valid_ticket:
        for idx, col in enumerate(tick):
            if int(col) in valid[w]:
                tick_ord[w][idx] += 1

for col_idx in range(len(valid_ticket[0])): # Look through eac col
    for w in orig_ord: # For each col check each category
        for tick in valid_ticket: ## For each ticket check if that column is in each category
            if int(tick[col_idx]) in valid[w]:
                tick_ord[w][col_idx] += 1


catch = [print(tick_ord[k])  for k in tick_ord ]
tick_ord2 = {}
for k in tick_ord:
    tmp = []
    for idx in tick_ord[k]:
        if tick_ord[k][idx] == len(valid_ticket):
            tmp.append(idx)
    tick_ord2[k] = tmp

for k in sorted(tick_ord2, key=lambda k: len(tick_ord2[k]), reverse=True):
    print(k, tick_ord2[k])

dep_idx = [18, 5, 4, 17, 15, 6]
my_tick = lines[22].split(",")
ans = 1
for i, v in enumerate(my_tick):
    if i in dep_idx:
        ans *= int(v)

print(ans)