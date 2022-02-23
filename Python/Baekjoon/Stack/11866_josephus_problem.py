'''
https://www.acmicpc.net/problem/11866
'''

import sys

input_ = sys.stdin.readline

n, k = map(int, input_().split())
numbers = list(range(1, n+1))
josephus = []
idx = 0

while numbers:
    idx = (idx+k-1)%len(numbers)
    josephus.append(str(numbers.pop(idx)))

print('<'+', '.join(josephus)+'>')
