# https://www.acmicpc.net/problem/1311

import sys

input_ = sys.stdin.readline

def get_minimum_effort(n, effort):
    dp = [float('inf')]*(1<<n)
    dp[0] = 0
    for path in range(1<<n):
        num_participated = count_ones(path)
        for work_idx in range(n):
            mask = 1<<work_idx
            if (not path&mask):
                dp[path|mask] = min(dp[path|mask], dp[path]+effort[num_participated][work_idx])
    return dp[-1]

def count_ones(n):
    count = 0
    while n:
        if (n&1):
            count += 1
        n>>=1
    return count

def main():
    n = int(input_())
    effort = [list(map(int, input_().split())) for _ in range(n)]
    print(get_minimum_effort(n, effort))


if __name__ == '__main__':
    main()
