'''
https://www.acmicpc.net/problem/7576
'''
import sys
from collections import deque

input_ = sys.stdin.readline

m, n = map(int, input_().split())

box = [input_().split() for _ in range(n)]
queue = deque()
tomato_left = 0
day = -1
dx_dy = ((1, 0), (0, 1), (-1, 0), (0, -1))


for x in range(n):
    for y in range(m):
        if box[x][y] == '1':
            queue.append((x, y))
        if box[x][y] == '0':
            tomato_left += 1

while queue:
    day += 1
    for _ in range(len(queue)):
        cur_x, cur_y = queue.popleft()
        for dx, dy in dx_dy:
            nxt_x, nxt_y = cur_x+dx, cur_y+dy
            if 0 <= nxt_x < n and 0 <= nxt_y < m and box[nxt_x][nxt_y] == '0':
                queue.append((nxt_x, nxt_y))
                box[nxt_x][nxt_y] = '1'
                tomato_left -= 1

if tomato_left != 0:
    print(-1)
else:
    print(day)