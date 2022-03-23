import sys
from collections import defaultdict

input_ = sys.stdin.readline
n, k = map(int, input_().split())
items = [tuple(map(int, input_().split())) for _ in range(n)]

def dict_knapsack():
    values = defaultdict(int)
    values[0] = 0

    for cur_weight, cur_value in items:
        keys = sorted(values.keys(), reverse=True)
        for last_weight in keys:
            added_weight = last_weight+cur_weight
            if added_weight > k:
                continue
            values[added_weight] = max(values[added_weight], values[last_weight]+cur_value)

    return max(values.values())

def ordinary_knapsack():
    dp = [[0]*(n+1) for _ in range(k+1)]
    for i in range(1, k+1):
        for j in range(1, n+1):
            weight = items[j-1][0]
            value = items[j-1][1]
            if weight > i:
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-weight][j-1]+value)
    return dp[k][n]

def fast_knapsack():
    dp = [0]*(k+1)
    for weight, value in items:
        for i in range(k, weight-1, -1):
            dp[i] = max(dp[i-weight]+value, dp[i])
    return dp[k]

