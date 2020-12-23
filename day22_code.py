import re
from itertools import combinations

root = "C:/Users/aiden/Dropbox/git/adventofcode/"
lines = [l.rstrip('\n') for l in open(root + 'day21_input.txt', 'r').readlines()]
flatten = lambda t: [item for sublist in t for item in sublist]

lines = open(root + 'day22_input.txt', 'r').read().split("\n\n")
p1 = lines[0].split(":")[1].strip().split("\n")
p2 = lines[1].split(":")[1].strip().split("\n")
p1 = [int(p) for p in p1]
p2 = [int(p) for p in p2]

while True:
    if p1 == [] or p2 == []:
        break
    p1_c = p1.pop(0)
    p2_c = p2.pop(0)
    if p1_c > p2_c:
        p1.append(p1_c)
        p1.append(p2_c)
    if p2_c > p1_c:
        p2.append(p2_c)
        p2.append(p1_c)

ans = 0
for i in range(len(p2)):
    ans += (len(p2) - i) * p2[i]


## Part 2

lines = [l.rstrip('\n') for l in open(root + 'day21_input.txt', 'r').readlines()]
flatten = lambda t: [item for sublist in t for item in sublist]

lines = open(root + 'day22_input.txt', 'r').read().split("\n\n")
p1 = lines[0].split(":")[1].strip().split("\n")
p2 = lines[1].split(":")[1].strip().split("\n")
p1 = [int(p) for p in p1]
p2 = [int(p) for p in p2]


rounds = []
def subgame(p1, p2):
    # print(f"Playing subround of cards p1 {len(p1)} cards {p1} and\np2 {len(p2)} cards {p2}")
    rounds = []
    while True:
        if p1 == [] or p2 == []:
            break
        p1_c = p1.pop(0)
        p2_c = p2.pop(0)
        if [p1_c, p2_c] in rounds or (len(p1) == 0 and len(p2) == 0):
            p1.append(p1_c)
            p1.append(p2_c)      
        if len(p1) >=p1_c and len(p2) >= p2_c:
            winner = subgame(p1[0:p1_c].copy(), p2[0:p2_c].copy())  
            if winner == 'p1':
                p1.append(p1_c)
                p1.append(p2_c)   
            else:
                p2.append(p2_c)
                p2.append(p1_c)
        else:
            if p1_c > p2_c:
                p1.append(p1_c)
                p1.append(p2_c)
            if p2_c > p1_c:
                p2.append(p2_c)
                p2.append(p1_c)
        rounds.append([p1_c, p2_c])                
    if p1 == []:
        return 'p2'
    elif p2 == []:
        return 'p1'

rounds = []
i = 0
while True:
    if p1 == [] or p2 == []:
        break
    p1_c = p1.pop(0)
    p2_c = p2.pop(0)
    if [p1_c, p2_c] in rounds or (len(p1) == 0 and len(p2) == 0):
        print(f"Round {i}... winner p1 cards {p1}")
        p1.append(p1_c)
        p1.append(p2_c)      
    if len(p1) >=p1_c and len(p2) >= p2_c:
        winner = subgame(p1[0:p1_c].copy(), p2[0:p2_c].copy())  
        if winner == 'p1':
            print(f"Round {i}... winner p1 cards {p1}")
            p1.append(p1_c)
            p1.append(p2_c)   
        else:
            print(f"Round {i}... winner p2 cards {p2}")
            p2.append(p2_c)
            p2.append(p1_c)
    else:
        if p1_c > p2_c:
            print(f"Round {i}... winner p1 cards {p1}")
            p1.append(p1_c)
            p1.append(p2_c)
        if p2_c > p1_c:
            print(f"Round {i}... winner p2 cards {p2}")
            p2.append(p2_c)
            p2.append(p1_c)    
    i += 1        
    rounds.append([p1_c, p2_c])



ans = 0
for i in range(len(p2)):
    ans += (len(p2) - i) * p2[i]

print(ans)