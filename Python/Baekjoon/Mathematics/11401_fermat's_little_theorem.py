'''
https://www.acmicpc.net/problem/11401
'''
import sys

input_ = sys.stdin.readline

n, k = map(int, input_().split())
p = 1000000007
numer = 1
denom = 1

def power(x, y):
    if y == 1:
        return x
    return power(x, y//2)**2%p if y%2 == 0 else power(x, y//2)**2*x%p

for i in range(k):
    numer = numer*(n-i)%p
    denom = denom*(i+1)%p

print(numer*power(denom, p-2)%p)
