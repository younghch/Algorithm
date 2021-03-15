"""
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
"""

import collections
import sys

# n = number of vertex, m = number of line
n, m = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(list)
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# idea : dfs?
