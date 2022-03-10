'''
https://www.acmicpc.net/problem/1012
'''
import sys
from collections import deque

input_ = sys.stdin.readline

def bfs(graph, point):
    queue = deque([point])
    graph[point] = False
    dl = (1, -1)
    while queue:
        a, b = queue.popleft()
        for d in dl:
            if (a+d, b) in graph and graph[(a+d, b)]:
                queue.append((a+d, b))
                graph[(a+d, b)] = False
            if (a, b+d) in graph and graph[(a, b+d)]:
                queue.append((a, b+d)) and graph[(a, b+d)]
                graph[(a, b+d)] = False


t = int(input_())
ans = []

for _ in range(t):
    m, n, k = map(int, input_().split())
    graph = {}
    count = 0

    for _ in range(k):
        x, y = map(int, input_().split())
        graph[(x , y)] = True
    
    for key in graph:
        if graph[key]:
            count+=1
            bfs(graph, key)
    ans.append(count)

print(*ans, sep='\n')
