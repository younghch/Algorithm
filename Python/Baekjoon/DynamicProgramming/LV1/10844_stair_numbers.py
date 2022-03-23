'''
https://www.acmicpc.net/problem/10844
'''

import sys

input_ = sys.stdin.readline

n = int(input_())
ends = [[0]*10 for _ in range(101)]

ends[1][0] = 0
for f in range(1, 10):
    ends[1][f] = 1

for i in range(2, n+1):
    ends[i][0] = ends[i-1][1]%1000000000
    for j in range(1, 9):
        ends[i][j] = (ends[i-1][j-1]+ends[i-1][j+1])%1000000000
    ends[i][9] = ends[i-1][8]%1000000000

print(sum(ends[n])%1000000000)

