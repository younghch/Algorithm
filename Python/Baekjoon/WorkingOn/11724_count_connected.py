"""
https://www.acmicpc.net/problem/11724
"""

import collections
import sys

sys.setrecursionlimit(10**6)

# n = number of vertex, m = number of line
n, m = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(list)
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# idea : dfs
been = [0 for _ in range(n)]
been.append(0)
been[0] = 1


def dfs(v):
    next_l = graph[v]
    for next_v in next_l:
        if been[next_v] == 1:
            continue
        been[next_v] = 1
        dfs(next_v)


ans = 0
idx = 0
while idx != -1:
    try:
        idx = been.index(0)
        ans += 1
        been[idx] = 1
        dfs(idx)
    except ValueError:
        idx = -1
print(ans)
