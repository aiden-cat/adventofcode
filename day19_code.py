import re
from itertools import combinations

root = "C:/Users/aiden/Dropbox/git/adventofcode/"
lines = [l.rstrip('\n') for l in open(root + 'day19_input.txt', 'r').readlines()]
flatten = lambda t: [item for sublist in t for item in sublist]

rules = {}
for l in lines[0:140]:
    num = l.split(":")[0]
    rule = l.split(":")[1].replace('"', '').strip().split(" ")
    rules[num] = rule

regex_ptrn = ''
start = rules['0']

rules['|'] = None
def resolve_rule(val, breaker):
    regex_ptrn = ''
    if any([x for x in ['8', '11'] if x in val]):
        breaker = 0
    i = 0
    if '|' in val:
        regex_ptrn += '('
    while True:
        # print(f"Working on idx {i} for val {val}")
        if i == (len(val)) or breaker >= 3:
            if '|' in val:
                regex_ptrn += ')'
            break        
        elif val[i] == '|':
            regex_ptrn += val[i]            
        elif rules[val[i]][0] in ['a', 'b']:
            regex_ptrn += rules[val[i]][0]
        else:
            regex_ptrn += resolve_rule(rules[val[i]], breaker)
        if val[i] in ['8', '11']:
            breaker += 1            
        i += 1
    return regex_ptrn


to_match_regex = '^' +  resolve_rule(rules['0'], 0) + '$'
num_match = 0
for line in lines[141:505]:
    if re.search(to_match_regex, line) is not None:
        num_match += 1

print(num_match)

## Part 2...
rules['8'] = '42 | 42 8'.split(" ")
rules['11'] = '42 31 | 42 11 31'.split(" ")

rule_8 = resolve_rule(rules['8'], 0)
rule_11 = resolve_rule(rules['11'], 0)
rule_42 = resolve_rule(rules['42'], 0)
rule_31 = resolve_rule(rules['31'], 0)

to_match_regex = '^' +  resolve_rule(rules['0'], 0) + '$'

to_match_regex = f"^{rule_8}{rule_11}$"
rule_8_exp = rule_8
rule_11_exp = rule_11
for i in range(2,15):
    rule_8_exp += f"|{rule_8 * i}"
    rule_11_exp += f"|{rule_42 * i}{rule_31 * i}"

to_match_regex = f"^({rule_8_exp})({rule_11_exp})$"
num_match = 0
for line in lines[141:505]:
    if re.search(to_match_regex, line) is not None:
        num_match += 1

print(num_match)