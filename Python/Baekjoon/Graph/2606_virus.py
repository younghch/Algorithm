'''
https://www.acmicpc.net/problem/2606
'''
import sys
from collections import defaultdict

input_ = sys.stdin.readline

n = int(input_())
graph = defaultdict(list)

def dfs_get_count():
    stack = [1]
    visited = [False]*(n+1)

    while stack:
        cur = stack.pop()
        visited[cur] = True
        for next_ in graph[cur]:
            if visited[next_]:
                continue
            stack.append(next_)

    return sum(visited)-1
        

for _ in range(int(input_())):
    a, b = map(int, input_().split())
    graph[a].append(b)
    graph[b].append(a)

print(dfs_get_count())
