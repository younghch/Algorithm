'''
https://www.acmicpc.net/problem/1260
'''
import sys
from collections import deque

input_ = sys.stdin.readline

n, m, v = map(int, input_().split())
graph = [[False]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input_().split())
    graph[a][b] = True
    graph[b][a] = True

def dfs(s):
    stack = [s]
    visited = []
    while stack:
        cur = stack.pop()
        if cur in visited:
            continue
        visited.append(cur)
        for next_ in range(n, 0, -1):
            if graph[cur][next_] and next_ not in visited:
                stack.append(next_)
    return visited

def bfs(s):
    queue = deque([s])
    visited = []
    while queue:
        cur = queue.popleft()
        if cur in visited:
            continue
        visited.append(cur)
        for next_ in range(1, n+1):
            if graph[cur][next_] and next_ not in visited:
                queue.append(next_)
    return visited

print(*dfs(v))
print(*bfs(v))
