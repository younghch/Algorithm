'''
https://www.acmicpc.net/problem/11053
'''

import sys
from collections import defaultdict

input_ = sys.stdin.readline

n = int(input_())
nums = list(map(int, input_().split()))
isChecked = defaultdict(lambda: True)
lenOfSeq = dict()

lenOfSeq[nums[-1]] = 1
for i in range(len(nums)-2, -1, -1):
    cur = nums[i]
    lenOfSeq[cur] = 1
    for key in lenOfSeq.keys():
        if key > cur:
            lenOfSeq[cur] = max(lenOfSeq[cur], 1+lenOfSeq[key])

print(max(lenOfSeq.values()))

