'''
https://www.acmicpc.net/problem/2110
'''
import sys

input_ = sys.stdin.readline

n, c = map(int, input_().split())
house = sorted([int(input_()) for _ in range(n)])
l = 0
r = house[-1]-house[0]

def get_count(d):
    current = house[0]
    count = 1
    for i in range(1, len(house)):
        if current+d <= house[i]:
            count += 1
            current = house[i]
    return count

def binary_search(l, r):
    while l <= r:
        mid = (l+r)//2
        if get_count(mid) >= c:
            l = mid+1
        else:
            r = mid-1
    return l-1

print(binary_search(l, r))
