'''
https://www.acmicpc.net/problem/11053
'''

import sys
from collections import deque

input_ = sys.stdin.readline

n = int(input_())
seq = enumerate(map(int, input_().split()))
dp = [[] for _ in range(n)]
idx = 0

dp[0].append(next(seq))
is_head_chagned = False
max_len = 1


for idx, num in seq:
    for i in range(max_len):
        if dp[i][-1][1] == num:
            break
        if dp[i][-1][1] > num:
            dp[i].append((idx, num))
            break
    if dp[max_len-1][-1][1] < num:
        dp[max_len].append((idx, num))
        max_len += 1

path = [dp[max_len-1][-1]]
ans = deque([str(path[-1][1])])
for i in range(max_len-2, -1, -1):
    last_idx, last_number = path[-1]
    for candidate in dp[i]:
        idx, val = candidate
        if idx < last_idx and val < last_number:
            path.append((idx, val))
            ans.appendleft(str(val))
            break

print(max_len)
print(' '.join(ans))
