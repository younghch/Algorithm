'''
https://www.acmicpc.net/problem/1003
'''

import sys

input = sys.stdin.readline

t = int(input())

fibo = [0]*40
fibo[0] = 1
fibo[1] = 1

def getFibo(n):
    if n < 0:
        return 0
    if fibo[n]:
        return fibo[n]
    fibo[n] = getFibo(n-1) + getFibo(n-2)
    return fibo[n]
        
def printNumberOfZeroOne(n):
    if n == 0:
        print(1, 0)
    else: 
        print(getFibo(n-2), getFibo(n-1))

for _ in range(t):
    printNumberOfZeroOne(int(input()))
