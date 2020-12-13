import re

root = "C:/Users/aiden/Dropbox/git/adventofcode/"
lines = [l.rstrip('\n') for l in open(root + 'day7_input.txt', 'r').readlines()]
flatten = lambda t: [item for sublist in t for item in sublist]

# Build Dict
bags = {}
for line in lines:
    col = re.search(".*?(?=bags)", line).group(0).strip()
    tmp = re.search("(?<=contain).*", line).group().strip()
    search = re.findall("(\d+)\s([\w\s]+)\s(?=bag)", tmp)
    for res in search:
        if col not in bags.keys():
            bags[col] = {res[1]: res[0]}
        else:
            bags[col].update({res[1]: res[0]})
    if search == [] :
        bags[col] = {}

search_res = {}
def search_col(col):
    # print(f"Working on {col}")
    if col in search_res.keys():
        return([search_res[col]])
    if 'shiny gold' in bags[col].keys():
        search_res[col] = True
        return [True]
    else:
        if col not in bags.keys():
            return [False]
        else:
            # print(bags[col])
            catch = flatten([search_col(s) for s in bags[col].keys()])
            if any(catch):
                search_res[col] = True
            else:
                search_res[col] = False
            # print(f"{col} found {catch} res in {any(catch)}")
            return [any(catch)]

catch = [search_col(col) for col in bags]
sum([1 for k in search_res.keys() if search_res[k]])


## Part 2 - count shiny gold bags
def count_bags(col):
    tot = 0
    for c in bags[col]:
        tot += int(bags[col][c]) + int(bags[col][c]) * count_bags(c)
    return tot

count_bags('shiny gold')