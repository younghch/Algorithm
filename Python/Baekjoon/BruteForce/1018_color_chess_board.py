'''
https://www.acmicpc.net/problem/1018
'''

import sys

WB = ('W', 'B')
BW = ('B', 'W')

def checkLine(type, line, board, row):
    for i in range(len(line)):
        if i%2==0 and line[i]!=type[0]:
            board[row][i] = True
        elif i%2==1 and line[i]!=type[1]:
            board[row][i] = True

def getSumOfEight(r, c, board):
    return sum([board[x][y] for x in range(r, r+8) for y in range(c, c+8)])

def main():
    n, m = map(int, sys.stdin.readline().split())
    board_W = [[False]*m for _ in range(n)]
    board_B = [[False]*m for _ in range(n)]
    board = [sys.stdin.readline().rstrip() for _ in range(n)]
    for i, line in enumerate(board):
        if i%2==0:
            checkLine(WB, line, board_W, i)
            checkLine(BW, line, board_B, i)
        else:
            checkLine(BW, line, board_W, i)
            checkLine(WB, line, board_B, i)
    ans = 64
    for i in range(n-7):
        for j in range(m-7):
            ans = min(ans, getSumOfEight(i, j, board_W))
            ans = min(ans, getSumOfEight(i, j, board_B))
    print(ans)

main()
