'''
https://www.acmicpc.net/problem/1931
'''

import sys

input_ = sys.stdin.readline

n = int(input_())
times = [tuple(map(int, input_().split())) for _ in range(n)]
count = 0
c_e = 0

times.sort(key=lambda x: (x[1], x[0]))
for time in times:
    if c_e <= time[0]:
        count+=1
        c_e = time[1]

print(count)
