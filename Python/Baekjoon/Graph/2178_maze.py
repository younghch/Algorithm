'''
https://www.acmicpc.net/problem/2178
'''
import sys
from collections import deque

input_ = sys.stdin.readline

n, m = map(int, input_().split())
maze = [['0']*(m+2)]
for _ in range(n):
    maze.append(['0']+list(input_().strip())+['0'])
maze.append(['0']*(m+2))
visited = [[False]*(m+2) for _ in range(n+2)]

def bfs():
    visited[1][1] = True
    dx_dy = ((1, 0), (0, 1), (-1, 0), (0, -1))
    queue = deque([(1, 1, 1)])

    while queue:
        x, y, count = queue.popleft()
        count += 1
        for dx, dy in dx_dy:
            next_x, next_y = x+dx, y+dy
            if next_x == n and next_y == m:
                return count
            if maze[next_x][next_y] == '1' and not visited[next_x][next_y]:
                visited[next_x][next_y] = True
                queue.append((next_x, next_y, count))
    return -1

print(bfs())
