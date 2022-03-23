'''
https://www.acmicpc.net/problem/1904
'''

import sys

input_ = sys.stdin.readline

t = int(input_())

def getFibo(n):
    a = 1
    b = 1
    ans = 1
    for _ in range(n-1):
        a = b
        b = ans
        ans = (a+b)%15746
    return ans
 
print(getFibo(t))
