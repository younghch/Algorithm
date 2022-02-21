'''
https://www.acmicpc.net/problem/11054
'''

import sys

input_ = sys.stdin.readline

n = int(input_())
numbers = list(map(int, input_().split()))

smallers = [numbers[0]]
largers = [numbers[-1]]
ans = [1]*n

def binarySearch(s, e, target, arr):
    mid = (s+e)//2
    if s > e:
        return s
    if arr[mid] < target:
        return binarySearch(mid+1, e, target, arr)
    else:
        return binarySearch(s, mid-1, target, arr)

def dpSmallers():
    for i in range(n):
        cur = numbers[i]
        if cur > smallers[-1]:
            ans[i] += len(smallers)
            smallers.append(cur)
        else:
            idx = binarySearch(0, len(smallers)-1, cur, smallers)
            ans[i] += idx
            smallers[idx] = cur
            

def dpLargers():
    for j in range(n-1, -1, -1):
        cur = numbers[j]
        if cur > largers[-1]:
            largers.append(cur)
            ans[j] += len(largers)-1
        else:
            idx = binarySearch(0, len(largers)-1, cur, largers)
            ans[j] += idx
            largers[idx] = cur

dpSmallers()
dpLargers()

print(max(ans))
