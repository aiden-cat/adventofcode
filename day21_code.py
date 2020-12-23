import re
from itertools import combinations

root = "C:/Users/aiden/Dropbox/git/adventofcode/"
lines = [l.rstrip('\n') for l in open(root + 'day21_input.txt', 'r').readlines()]
flatten = lambda t: [item for sublist in t for item in sublist]

t_lines = open(root + 'day21_input.txt', 'r').read().split("\n\n")
allergens = {}
ings = []
for line in lines:
    ingredients = re.search(".*(?= \()", line).group(0)
    allerg = re.search("(?<=contains ).*(?=\))", line).group(0)
    ings.append(ingredients.split(" "))
    for a in allerg.split(", "):
        if a not in allergens:
            allergens[a] = [ingredients.split(" ")]
        else:
            allergens[a].append(ingredients.split(" "))

ans = {}
for a in allergens:
    a_tmp = set.intersection(*map(set, allergens[a]))
    ans[a] = list(a_tmp)

for a in sorted(ans, key=lambda k: len(ans[k])):
    for el in ans[a]:
        to_search = [x for x in ans if x != a]
        for a2 in to_search:
            ans[a2] = [x for x in ans[a2] if x != el]

ings = flatten(ings)
to_rem = flatten(ans[k] for k in ans)
len([x for x in ings if x not in to_rem])

## Part 2
dairy: [vcckp]
eggs: [hjz]
fish: [nhvprqb]
nuts: [jhtfzk]
peanuts: [mgkhhc]
sesame: [qbgbmc]
shellfish: [bzcrknb]
wheat: [zmh]

## Modify in sublime