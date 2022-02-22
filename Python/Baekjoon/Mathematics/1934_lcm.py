'''
https://www.acmicpc.net/problem/1934
'''
import sys

input_ = sys.stdin.readline

def getGCD(a, b):
    if b == 0:
        return a
    return getGCD(b, a%b)

def getLCM(a, b):
    return a*b//getGCD(a,b)

n = int(input_())
for _ in range(n):
    print(getLCM(*map(int, input_().split())))
