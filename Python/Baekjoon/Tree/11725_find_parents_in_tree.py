'''
https://www.acmicpc.net/problem/11725
'''
import sys
from collections import defaultdict, deque

input_ = sys.stdin.readline

n = int(input_())
lines = defaultdict(list)
for _ in range(n-1):
    a, b = map(int, input_().split())
    lines[a].append(b)
    lines[b].append(a)

def find_parents_bfs(lines):
    parents = [0]*(n)
    parents[0] = 1
    queue = deque([1])
    while queue:
        parent = queue.popleft()
        for child in lines[parent]:
            if parents[child-1]:
                continue
            parents[child-1] = parent
            queue.append(child)

    return parents[1:]

print(*find_parents_bfs(lines), sep='\n')
