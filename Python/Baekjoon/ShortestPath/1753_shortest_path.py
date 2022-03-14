'''
https://www.acmicpc.net/problem/1753
'''
import sys
from collections import defaultdict
import heapq

input_ = sys.stdin.readline

v, e = map(int, input_().split())
k = int(input_())

graph = defaultdict(list)
for _ in range(e):
    a, b, w = map(int, input_().split())
    graph[a].append((w, b))

def dijkstra():
    dist = [float('inf')]*(v+1)
    dist[k] = 0
    pq = []

    heapq.heappush(pq, (0, k))
    while pq:
        w_cur, v_cur = heapq.heappop(pq)
        for w_next, v_next in graph[v_cur]:
            alt = w_cur+w_next
            if dist[v_next] > alt:
                dist[v_next] = alt
                heapq.heappush(pq, (alt, v_next))
    return dist

dist = map(lambda x: 'INF' if x == float('inf') else str(x), dijkstra()[1:])
print('\n'.join(dist))
