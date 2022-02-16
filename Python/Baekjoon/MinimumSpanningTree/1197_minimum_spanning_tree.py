"""
https://www.acmicpc.net/problem/1197
"""

import sys


v, e = map(int, sys.stdin.readline().split())
graph = []
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph.append((c, a, b))
if v == 1:
    print(0)
else:
    group = dict()
    for i in range(v):
        group[i + 1] = i + 1


    def find(x):
        if group[x] == x:
            return x
        else:
            return find(group[x])


    def union(x, y):
        x_root = find(x)
        y_root = find(y)
        if x_root > y_root:
            x_root, y_root = y_root, x_root
        group[y_root] = x_root


    graph.sort()
    ans = 0
    for c, a, b in graph:
        if find(a) != find(b):
            union(a, b)
            ans += c
    print(ans)
