'''
https://www.acmicpc.net/problem/2805
Croatian Open Competition in Informatics > COCI 2011/2012 > Contest #5
'''
import sys

input_ = sys.stdin.readline

n, target = map(int, input_().split())
trees = list(map(int, input_().split()))

def get_highest():
    l = 0
    r = max(trees)-1

    while l <= r:
        mid = (l+r)//2
        amount = sum(map(lambda x: max(x-mid, 0), trees))
        if amount > target:
            l = mid+1
        elif amount == target:
            return mid
        else:
            r = mid-1
    return r

print(get_highest())
