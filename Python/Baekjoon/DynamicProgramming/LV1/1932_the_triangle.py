'''
https://www.acmicpc.net/problem/1932
'''

import sys

input_ = sys.stdin.readline
n = int(input_())
board = [list(map(int, input_().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            board[i][j] = board[i-1][j] + board[i][j]
        elif j == i:
            board[i][j] = board[i-1][j-1] + board[i][j]
        else:
           board[i][j] = max(board[i-1][j-1], board[i-1][j])+board[i][j]

print(max(board[n-1]))
