'''
https://www.acmicpc.net/problem/1300

'''

import sys

input_ = sys.stdin.readline

n = int(input_())
k = int(input_())


def count_smaller(x):
    count = 0
    for i in range(1, min(x, n+1)):
        count += min((x-1)//i, n)
    return count;

def binary_search(l, r):
    while (l <= r):
        mid = (l+r)//2
        smaller = count_smaller(mid)
        if (smaller == k-1):
            return mid
        if (smaller < k-1):
            l = mid+1
        else:
            r = mid-1
    return r

def approximate_in_square(y):
    diff = float('inf')
    
    for i in range(1, n+1):
        mod = y%i
        div = y//i
        if mod == 0 and div <= n:
            return y
        if div < n:
            diff = min(diff, (div+1)*i-y)
    return y+diff

print(approximate_in_square(binary_search(1, k)))
