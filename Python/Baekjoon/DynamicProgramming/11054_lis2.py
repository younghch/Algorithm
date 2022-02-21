import sys
'''
https://www.acmicpc.net/problem/11054
'''

import sys

input_ = sys.stdin.readline

n = int(input_())
numbers = list(map(int, input_().split()))

smallers = [0]*n
smallersReverse = [0]*n

smallers[0]=1
smallersReverse[-1]=1

def getSmaller(idx):
    val = numbers[idx]
    length = 1
    for i in range(idx-1, -1, -1):
        cur = numbers[i]
        if cur == val:
            length = max(length, smallers[i])
            break
        if cur < val:
            length = max(length, smallers[i]+1)
    smallers[idx] = length

def getSmallerReverse(idx):
    val = numbers[idx]
    length = 1
    for i in range(idx+1, len(numbers)):
        cur = numbers[i]
        if cur == val:
            length = max(length, smallersReverse[i])
            break
        if cur < val:
            length = max(length, smallersReverse[i]+1)
    smallersReverse[idx] = length

for i in range(1, n):
    getSmaller(i)
    getSmallerReverse(n-1-i)

print(max([x+y for x,y in zip(smallers, smallersReverse)])-1)

