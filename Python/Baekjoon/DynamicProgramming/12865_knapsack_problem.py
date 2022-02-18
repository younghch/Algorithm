import sys
from collections import defaultdict

input_ = sys.stdin.readline

n, k = map(int, input_().split())
items = [tuple(map(int, input_().split())) for _ in range(n)]
values = defaultdict(int)
values[0] = 0

for cur_weight, cur_value in items:
    keys = sorted(values.keys(), reverse=True)
    for last_weight in keys:
        added_weight = last_weight+cur_weight
        if added_weight > k:
            continue
        values[added_weight] = max(values[added_weight], values[last_weight]+cur_value)

print(max(values.values()))
