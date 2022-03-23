'''
https://www.acmicpc.net/problem/15681
'''
import sys

input_ = sys.stdin.readline

n, r, q = map(int, input_().split())
graph = [[] for _ in range(n+1)]
size_of_subtree = [1]*(n+1)

for _ in range(n-1):
    u, v = map(int, input_().split())
    graph[u].append(v)
    graph[v].append(u)

def update_size_of_subtree(root):
    stack = [(root, 0)]
    path = []
    while stack:
        parent, grand_parent = stack.pop()
        for child in graph[parent]:
            if child != grand_parent:
                stack.append((child, parent))
                path.append((child, parent))
    for child, parent in reversed(path):
        size_of_subtree[parent] += size_of_subtree[child]

update_size_of_subtree(r)

ans = [size_of_subtree[int(input_())] for _ in range(q)]
print(*ans, sep='\n')
