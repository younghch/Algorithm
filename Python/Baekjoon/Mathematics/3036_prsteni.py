'''
https://www.acmicpc.net/problem/3036
'''

import sys

input_ = sys.stdin.readline

def getGCD(a, b):
    return getGCD(b, a%b) if a%b else b

int(input_())
rings = map(int, input_().split())
first = next(rings)

for ring in rings:
    gcd = getGCD(first, ring)
    print(f'{first//gcd}/{ring//gcd}')
