'''
https://www.acmicpc.net/problem/1010
'''

import sys

input_ = sys.stdin.readline

n = int(input_())

def getBinomialCoefficient(n, k):
    res = 1
    for i in range(1, k+1):
        res = res*(n+1-i)//i
    return res

for _ in range(n):
    n, k = map(int, input_().split())
    if n < k:
        n, k = k, n
    print(getBinomialCoefficient(n, k))
