'''
https://www.acmicpc.net/problem/1504
'''
import sys
from collections import defaultdict
import heapq

input_ = sys.stdin.readline

n, e = map(int, input_().split())
graph = defaultdict(list)

for _ in range(e):
    a, b, w = map(int, input_().split())
    graph[a].append((w, b))
    graph[b].append((w, a))

def dijkstra(start, end):
    pq = []
    heapq.heappush(pq, (0, start))
    dist = [float('inf')]*(n+1)
    visited = [False]*(n+1)

    while pq:
        c_w, c_v = heapq.heappop(pq)
        if c_v == end:
            return c_w
        for n_w, n_v in graph[c_v]:
            if visited[n_v]:
                continue
            alt = n_w+c_w
            if dist[n_v] > alt:
                dist[n_v] = alt
                heapq.heappush(pq, (alt, n_v))
    return -1

def shortest_path(v1, v2):
    s_v1, s_v2, v1_v2, v1_e, v2_e = dijkstra(1, v1), dijkstra(1, v2), dijkstra(v1, v2), dijkstra(v1, n), dijkstra(v2, n)
    route_1, route_2 = float('inf'), float('inf')
    
    if v1_v2 == -1:
        return -1   
    if s_v1 != -1 and v2_e != -1:
        route_1 = s_v1+v1_v2+v2_e
    if s_v2 != -1 and v1_e != -1:
        route_2 = s_v2+v1_v2+v1_e

    shortest = min(route_1, route_2)
    if shortest == float('inf'):
        return -1
    return shortest

print(shortest_path(*map(int, input_().split())))
