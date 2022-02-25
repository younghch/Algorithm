import sys
from collections import deque

'''
https://www.acmicpc.net/problem/5430
'''

input_ = sys.stdin.readline

t = int(input_())
isReverse = False

def r():
    global isReverse
    isReverse = not isReverse

def d(queue):
    if isReverse:
        queue.pop()
    else:
        queue.popleft()

for _ in range(t):
    isReverse = False
    command = input_().rstrip()
    input_()
    queue = deque(input_()[1:-2].split(','))
    if queue[0] == '':
        queue.pop()
    try:
        for c in command:
            r() if c == 'R' else d(queue)
        toPrint = ','.join(list(queue)[::-1] if isReverse else list(queue))
        print(f'[{toPrint}]')
    except:
        print('error')
