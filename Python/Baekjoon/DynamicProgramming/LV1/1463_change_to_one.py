'''
https://www.acmicpc.net/problem/1463
'''

import sys

input_ = sys.stdin.readline

n = int(input_())
counts = [0] * 1000001
counts[2], counts[3] = 1, 1

for i in range(4,n+1):
    counts[i] = min(counts[i-1]+1, counts[i//2]+i%2+1, counts[i//3]+i%3+1)

print(counts[n])

