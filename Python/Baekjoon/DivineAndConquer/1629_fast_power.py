'''
https://www.acmicpc.net/problem/1629
'''
import sys

input_ = sys.stdin.readline

a, b, c = map(int, input_().split())
mod = a%c

def power(n):
    if n == 1:
        return mod
    elif n%2 == 0:
        return power(n//2)**2%c
    else:
        return power(n//2)**2*mod%c

print(power(b))

# if use built-in function
# print(pow(a, b, c))
