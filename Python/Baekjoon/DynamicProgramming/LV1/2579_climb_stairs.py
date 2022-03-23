'''
https://www.acmicpc.net/problem/2579
'''

import sys

input_ = sys.stdin.readline

n = int(input_())

def getScore(n):
    stairs = [int(input_()) for _ in range(n)]
    acc = [(stairs[0], 0), (stairs[1], stairs[0]+stairs[1])]
    for i in range(2, n):
        score = stairs[i]
        acc.append((max(acc[i-2])+score, acc[i-1][0]+score))
    return max(acc[n-1])

if n == 1:
    print(input_())
else:
    print(getScore(n))

