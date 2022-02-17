'''
https://www.acmicpc.net/problem/1912
'''

import sys

input_ = sys.stdin.readline

n = int(input_())
numbers = list(map(int, input_().split()))
acc = [numbers[0]]

for i in range(0, n-1):
    acc.append(max(acc[i]+numbers[i+1], numbers[i+1]))

print(max(acc))
