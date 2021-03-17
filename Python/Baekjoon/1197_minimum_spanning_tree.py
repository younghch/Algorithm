"""
그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하는 프로그램을 작성하시오.

최소 스패닝 트리는, 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리를 말한다.
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
