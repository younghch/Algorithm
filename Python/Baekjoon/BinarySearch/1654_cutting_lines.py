"""
https://www.acmicpc.net/problem/1654
"""
import sys

input_ = sys.stdin.readline

k, n = map(int, input_().split())
lines = [int(input_()) for _ in range(k)]
l = 1
r = max(lines)

def binary_search(l, r):
    if l > r:
        return r
    mid = (l+r)//2
    tot = sum(map(lambda x: x//mid, lines))
    if tot < n:
        return binary_search(l, mid-1)
    else:
        return binary_search(mid+1, r)

print(binary_search(l, r))
