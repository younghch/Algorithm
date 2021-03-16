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

graph.sort()
ans = graph[0][0]
# list of sets
segments = [set((graph[0][1], graph[0][2]))]
for info in graph:
    if len(segments[0]) == v:
        break
    c, a, b = info
    is_new = True
    is_bridge = -1
    for idx, segment in enumerate(segments):
        if a in segment and b in segment:
            is_new = False
            break
        if a in segment or b in segment:
            if is_bridge == -1:
                is_bridge = idx
                segment.update([a, b])
            else:
                segments[is_bridge].union(segment)
                segments.pop(idx)
                break
    if is_new:
        ans += c
    else:
        continue
print(ans)
