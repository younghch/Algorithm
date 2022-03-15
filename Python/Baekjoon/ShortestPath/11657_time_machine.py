'''
https://www.acmicpc.net/problem/11657
'''

import sys

input_ = sys.stdin.readline

v, e = map(int, input_().split())
edges = [tuple(map(int, input_().split())) for _ in range(e)]

def bellman_ford():
    dist = [float('inf')]*(v+1)
    dist[1] = 0
    for _ in range(v-1):
        for s, e, w in edges:
            if dist[s] != float('inf'):
                alt = dist[s]+w
                if dist[e] > alt:
                    dist[e] = alt
    negative_cycle = False
    for s, e, w in edges:
            if dist[s] != float('inf'):
                alt = dist[s]+w
                if dist[e] > alt:
                    dist[e] = alt
                    negative_cycle = True
    if negative_cycle:
        return [-1]
    return map(lambda x: -1 if x == float('inf') else x, dist[2:])

print(*bellman_ford(), sep='\n')

