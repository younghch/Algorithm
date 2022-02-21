'''
https://www.acmicpc.net/problem/11399
'''

import sys
from itertools import accumulate

input_ = sys.stdin.readline

input_()
times = list(map(int, input_().split()))

times.sort()
acc = accumulate(times)

print(sum(acc))
