'''
https://www.acmicpc.net/problem/9184
'''

import sys
from collections import defaultdict

input_ = sys.stdin.readline

w = defaultdict(int)

def getW(x, y, z):
    if x<1 or y <1 or z<1:
        return 1
    if w[(x, y, z)]:
        return w[(x, y, z)]
    if x>20 or y>20 or z>20:
        return getW(20, 20, 20)
    if x<y<z:
        w[(x, y, z)] = getW(x, y, z-1)+getW(x,y-1,z-1)-getW(x,y-1,z)
        return w[(x, y, z)]
    w[(x, y, z)] = getW(x-1, y, z) + getW(x-1, y-1, z) + getW(x-1, y, z-1) - getW(x-1, y-1, z-1)
    return w[(x, y, z)]

while True:
    cor = tuple(map(int, input_().split()))
    if cor == (-1, -1, -1):
        break
    print(f'w{cor} = {getW(*cor)}')
