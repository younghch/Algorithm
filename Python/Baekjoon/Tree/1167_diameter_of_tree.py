'''
https://www.acmicpc.net/problem/1167
'''
import sys

sys.setrecursionlimit(100000)
input_ = sys.stdin.readline

v = int(input_())
graph = [[] for _ in range(v+1)]

for _ in range(v):
    in_ = map(int, input_().split())
    a = next(in_)
    while (b := next(in_)) != -1:
        graph[a].append((b, next(in_)))

visited = [False]*(v+1)
max_dist = 0

def recursive_next_weight(c_v):
    global max_dist
    visited[c_v] = True
    c_w = 0
    for n_v, n_d in graph[c_v]:
        if not visited[n_v]:
            t_w = n_d+recursive_next_weight(n_v)
            max_dist = max(max_dist, c_w+t_w)
            c_w = max(c_w, t_w)
    return c_w

recursive_next_weight(1)
print(max_dist)