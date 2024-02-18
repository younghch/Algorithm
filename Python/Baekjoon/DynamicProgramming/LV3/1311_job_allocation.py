# https://www.acmicpc.net/problem/1311

import sys

input_ = sys.stdin.readline

n = int(input_())
effort = [list(map(int, input_().split())) for _ in range(n)]
dp = [float('inf')]*(2**n)
dp[0] = 0

for person in range(n):
    before_dp = [v for v in dp]
    for work_idx in range(n):
        mask = 1<<work_idx
        for visited in range(2**n):
            if visited&mask:
                continue
            dp[visited|mask] = min(before_dp[visited]+effort[person][work_idx], dp[visited|mask])
print(dp[-1])