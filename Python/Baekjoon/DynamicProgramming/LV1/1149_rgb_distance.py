'''
https://www.acmicpc.net/problem/1149
'''

import sys

input_ = sys.stdin.readline
n = int(input_())
board = [list(map(int, input_().split())) for _ in range(n)]

for i in range(1, len(board)):
    board[i][0] = min(board[i-1][1], board[i-1][2])+board[i][0]
    board[i][1] = min(board[i-1][0], board[i-1][2])+board[i][1]
    board[i][2] = min(board[i-1][0], board[i-1][1])+board[i][2]

print(min(board[n-1][0], board[n-1][1], board[n-1][2]))
