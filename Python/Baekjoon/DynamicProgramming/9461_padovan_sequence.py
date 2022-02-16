'''
https://www.acmicpc.net/problem/9461
'''

import sys

input = sys.stdin.readline

t = int(input())
fibo = [1 if i <3 else 0 for i in range(100)]

def getFibo(n):
    if not fibo[n]:
        fibo[n] = getFibo(n-3)+getFibo(n-2)
    return fibo[n]

for _ in range(t):
    print(getFibo(int(input())-1))
