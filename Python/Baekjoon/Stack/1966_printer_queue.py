'''
https://www.acmicpc.net/problem/1966
'''

import sys
from collections import deque

input_ = sys.stdin.readline

t = int(input_())

def getOrder():
    _, m = map(int, input_().split())
    importance = list(map(int, input_().split()))
    queue = deque([x, False] for x in importance)
    queue[m][1] = True
    importance.sort()

    order = 0
    while importance:
        to_print = importance.pop()
        while True:
            current_print = queue.popleft()
            if to_print != current_print[0]:
                queue.append(current_print)
                continue
            order += 1
            if current_print[1]:
                return order
            break

for _ in range(t):
    print(getOrder())
