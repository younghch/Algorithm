'''
https://www.acmicpc.net/problem/2004
'''

import sys

input_ = sys.stdin.readline

n, m = map(int, input_().split())

def getCount(k, n):
    div = k
    count = 0

    while n//div != 0:
        count += n//div
        div *= k
    return count

def getCountOf(k, n, m):
    return getCount(k, n)-getCount(k, n-m)-getCount(k, m)

print(min(getCountOf(2, n, m), getCountOf(5, n, m)))
