'''
https://www.acmicpc.net/problem/9375
'''

import sys
from collections import defaultdict

input_ = sys.stdin.readline

t = int(input_())

def getNumberOfCombination(n):
    clothes = defaultdict(int)
    for _ in range(n):
        _, category = input_().split()
        clothes[category] += 1
    comb = 1
    for count in clothes.values():
        comb *= count+1
    return comb - 1

for _ in range(t):
    print(getNumberOfCombination(int(input_())))
    