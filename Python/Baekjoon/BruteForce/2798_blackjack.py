'''
https://www.acmicpc.net/problem/2798
'''

import sys
from itertools import combinations

def getNeareastSum(m, cards):
    diff = 300000
    ans = 0
    for s in map(sum, combinations(cards, 3)):
        if s > m: continue
        else:
            new_diff = m-s
            if new_diff < diff:
                ans = s
                diff = new_diff
    return ans


def main():
    n, m = map(int, sys.stdin.readline().split())
    cards = map(int, sys.stdin.readline().split())
    print(getNeareastSum(m, cards))

main()
