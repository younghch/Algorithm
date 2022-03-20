'''
https://www.acmicpc.net/problem/1717
'''
import sys

input_ = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, m = map(int, input_().split())
roots = dict()
to_print = []

for i in range(n+1):
    roots[i] = i

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    roots[root_a] = root_b

def find(a):
    root = roots[a]
    if root != a:
        roots[a] = find(root)
    return roots[a]

def is_subset(a, b):
    return 'YES' if find(a) == find(b) else 'NO'

for _ in range(m):
    command, a, b = map(int, input_().split())
    if not command:
        union(a, b)
    else:
        to_print.append(is_subset(a, b))

print('\n'.join(to_print))
