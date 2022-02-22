'''
https://www.acmicpc.net/problem/2609
'''

import sys

input_ = sys.stdin.readline

def getGCD(a, b):
    if b == 0:
        return a
    return getGCD(b, a%b)

def getLCM(a, b, gcd):
    return a*b//gcd

a, b = map(int, input_().split())
if a < b:
    a, b = b, a

gcd = getGCD(a, b)
lcm = getLCM(a, b, gcd)

print(gcd, lcm, sep='\n')
