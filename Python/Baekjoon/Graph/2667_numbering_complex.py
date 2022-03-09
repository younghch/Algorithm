'''
https://www.acmicpc.net/problem/2667
'''

import sys

input_ = sys.stdin.readline

n = int(input_())
square = [list(input_().rstrip()) for _ in range(n)]
complex_ = []

def dfs_get_count(x, y):
    ds = (1, -1)
    stack = [(x, y)]
    visited = []
    while stack:
        cur = stack.pop()
        if cur in visited:
            continue
        visited.append(cur)
        c_x, c_y = cur
        square[c_x][c_y] = '0'
        for d in ds:
            if 0 <= c_x+d < n and square[c_x+d][c_y] == '1':
                stack.append((c_x+d, c_y))
            if 0 <= c_y+d < n and square[c_x][c_y+d] == '1':
                stack.append((c_x, c_y+d))
    return len(visited)

for x in range(n):
    for y in range(n):
        if square[x][y] == '1':
            complex_.append(dfs_get_count(x, y))

complex_.sort()
print(len(complex_), *complex_, sep='\n')
