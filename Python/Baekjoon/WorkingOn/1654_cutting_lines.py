"""
https://www.acmicpc.net/problem/1654
"""

import sys

k, n = map(int, sys.stdin.readline().split())
lines = []
for _ in range(k):
    lines.append(int(sys.stdin.readline()))
ans = sum(lines) // n + 1
ten = 1
while ten <= ans // 10:
    ten *= 10
count = 0


def find_ten_power_down(d, c_len):
    made = 0
    while made < n:
        c_len -= d
        made = 0
        for line in lines:
            made += line // c_len
    return c_len + d


def find_ten_power_up(d, c_len):
    made = 0
    while made >= n:
        c_len += d
        made = 0
        for line in lines:
            made += line // c_len
    return c_len - d


while ten != 0:
    if count % 2 == 0:
        ans = find_ten_power_down(ten, ans)
    else:
        ans = find_ten_power_up(ten, ans)
    ten = ten // 10
if count % 2 == 0:
    ans -= 1
else:
    ans += 1

print(ans)
