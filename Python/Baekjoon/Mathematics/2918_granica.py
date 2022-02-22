'''
https://www.acmicpc.net/problem/2981
Croatian Open Competition in Informatics > COCI 2007/2008 > Contest #6 > no.3
'''

import sys

input_ = sys.stdin.readline

def getGCD(arr):
    min_ = min(arr)
    next_arr = []
    for num in arr:
        next_ = num % min_
        if next_ != 0:
            next_arr.append(next_)
    if not next_arr:
        return min_
    else:
        next_arr.append(min_)
        return getGCD(next_arr)

def getDivisors(m):
    seq = []
    rev = []
    for i in range(2, int(m**0.5)+1):
        if m%i == 0:
            seq.append(i)
            pair = m//i
            if i != pair:
                rev.append(pair)
    return [*seq, *rev[::-1], m]

n = int(input_())

numbers = [int(input_()) for _ in range(n)]
subs = []
for i in range(n):
    for j in range(i+1, n):
        subs.append(abs(numbers[i]-numbers[j]))
gcd = getGCD(subs)

print(*getDivisors(gcd))
