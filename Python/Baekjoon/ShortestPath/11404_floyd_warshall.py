'''
https://www.acmicpc.net/problem/11657
'''

import sys

input_ = sys.stdin.readline

n = int(input_())
m = int(input_())

def floyd_warshall():
    dist = [[float('inf')]*(n) for _ in range(n)]

    for _ in range(m):
        a, b, w = map(int, input_().split())
        dist[a-1][b-1] = min(dist[a-1][b-1], w)
    for i in range(n):
        dist[i][i] = 0
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
    return dist

def print_result():
    dist = floyd_warshall()
    for line in dist:
        print(*map(lambda x: 0 if x == float('inf') else x, line))

print_result()
