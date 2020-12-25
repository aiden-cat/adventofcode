import re
from itertools import combinations

root = "C:/Users/aiden/Dropbox/git/adventofcode/"
lines = [l.rstrip('\n') for l in open(root + 'day25_input.txt', 'r').readlines()]
flatten = lambda t: [item for sublist in t for item in sublist]

lines = open(root + 'day25_input.txt', 'r').read().split("\n\n")
def encrypt(base, loop):
    val = 1
    for i in range(loop):
        val *= base
        val = val % 20201227 
    return val

def decrypt(base, target):
    val = 1
    i = 1
    while True:
        val *= base
        val = val % 20201227
        if val == target:
            break
        i += 1
    return i

card_loop = encrypt(8790390, decrypt(7, 18499292))
encrypt(18499292, decrypt(7, 8790390))