"""
스타트링크에서 판매하는 어린이용 장난감 중에서 가장 인기가 많은 제품은 구슬 탈출이다. 구슬 탈출은 직사각형 보드에 빨간 구슬과 파란 구슬을 하나씩 넣은 다음, 빨간 구슬을 구멍을 통해 빼내는 게임이다.

보드의 세로 크기는 N, 가로 크기는 M이고, 편의상 1×1크기의 칸으로 나누어져 있다. 가장 바깥 행과 열은 모두 막혀져 있고, 보드에는 구멍이 하나 있다. 빨간 구슬과 파란 구슬의 크기는 보드에서 1×1크기의 칸을 가득 채우는 사이즈이고, 각각 하나씩 들어가 있다. 게임의 목표는 빨간 구슬을 구멍을 통해서 빼내는 것이다. 이때, 파란 구슬이 구멍에 들어가면 안 된다.

이때, 구슬을 손으로 건드릴 수는 없고, 중력을 이용해서 이리 저리 굴려야 한다. 왼쪽으로 기울이기, 오른쪽으로 기울이기, 위쪽으로 기울이기, 아래쪽으로 기울이기와 같은 네 가지 동작이 가능하다.

각각의 동작에서 공은 동시에 움직인다. 빨간 구슬이 구멍에 빠지면 성공이지만, 파란 구슬이 구멍에 빠지면 실패이다. 빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패이다. 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다. 또, 빨간 구슬과 파란 구슬의 크기는 한 칸을 모두 차지한다. 기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지이다.

보드의 상태가 주어졌을 때, 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 구하는 프로그램을 작성하시오.
"""

import sys
import collections

n, m = map(int, sys.stdin.readline().split())

table = []
wall, empty, goal, red, blue = '#', '.', 'O', 'R', 'B'
for i in range(n):
    line = list(sys.stdin.readline())
    if 'R' in line:
        red_loc = (i, line.index('R'))
        line[red_loc[1]] = empty
    if 'B' in line:
        blue_loc = (i, line.index('B'))
        line[blue_loc[1]] = empty
    table.append(line)
queue = collections.deque()
answer = [-1]
dxs, dys = (-1, 0, 1, 0), (0, -1, 0, 1)


def move(x, y, dx, dy):
    while table[x][y] == empty:
        x += dx
        y += dy
    if table[x][y] == wall:
        x -= dx
        y -= dy
    return x, y


def bfs(rx, ry, bx, by, depth):
    if depth == 11:
        return
    for j in range(4):
        dx, dy = dxs[j], dys[j]
        new_rx, new_ry = move(rx, ry, dx, dy)
        new_bx, new_by = move(bx, by, dx, dy)
        if table[new_bx][new_by] == goal:
            continue
        if table[new_rx][new_ry] == goal:
            answer[0] = depth
            break
        if new_rx == new_bx and new_ry == new_by:
            if dx != 0:
                if rx < bx:
                    queue.append((new_rx - 1, new_ry, new_bx, new_by, depth + 1))
                else:
                    queue.append((new_rx, new_ry, new_bx - 1, new_by, depth + 1))
            else:
                if ry < by:
                    queue.append((new_rx, new_ry - 1, new_bx, new_by, depth + 1))
                else:
                    queue.append((new_rx, new_ry, new_bx, new_by - 1, depth + 1))
        else:
            queue.append((new_rx, new_ry, new_bx, new_by, depth + 1))


queue.append((red_loc[0], red_loc[1], blue_loc[0], blue_loc[1], 1))


while answer[0] == -1 and queue:
    bfs(*queue.popleft())
print(answer[0])




