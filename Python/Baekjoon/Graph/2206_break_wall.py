'''
https://www.acmicpc.net/problem/2206
'''
import sys
from collections import deque

input_ = sys.stdin.readline

def bfs_break_wall():
    queue = deque([(0, 0, False, 1)])
    visited = {(0, 0)}
    visited_broken = set()
    dl = ((1, 0), (0, 1), (-1, 0), (0, -1))
    
    

    while queue:
        x, y, broken, depth = queue.popleft()
        if (x, y) == (n-1, m-1):
            return depth

        depth += 1
        for dx, dy in dl:
            next_x = x+dx
            next_y = y+dy
            next_ = (next_x, next_y)

            if next_x == -1 or next_x == n or next_y == -1 or next_y == m:
                continue
            if graph[next_x][next_y] == '0':                
                if not broken and next_ not in visited:
                    visited.add(next_)
                    queue.append((*next_, broken, depth))
                elif broken and next_ not in visited and next_ not in visited_broken:
                    visited_broken.add(next_)
                    queue.append((*next_, broken, depth))
            elif not broken:
                visited_broken.add(next_)
                queue.append((*next_, True, depth))
    return -1

n, m = map(int, input_().split())
graph = [list(list(input_().rstrip())) for _ in range(n)]

print(bfs_break_wall())
