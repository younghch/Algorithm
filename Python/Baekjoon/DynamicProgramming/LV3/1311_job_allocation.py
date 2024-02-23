# https://www.acmicpc.net/problem/1311

import sys

input_ = sys.stdin.readline

def count_ones(n):
    count = 0
    while n:
        if (n&1):
            count += 1
        n>>=1
    return count

n = int(input_())
effort = [list(map(int, input_().split())) for _ in range(n)]
dp = [float('inf')]*(1<<n)
dp[0] = 0

for person in range(n):
    for path in range(1<<n):
        if count_ones(path) == person:
            for i in range(n):
                mask = 1<<i
                if (not path&mask):
                    dp[path|mask] = min(dp[path|mask], dp[path]+effort[person][i])

print(dp[-1])