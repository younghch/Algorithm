'''
https://www.acmicpc.net/problem/2630
'''
import sys

input_ = sys.stdin.readline

n =  int(input_())
square = [list(map(int, input_().split())) for _ in range(n)]
white = 0
blue = 0

def check_and_add(x, y, l):
    global blue
    global white
    isBlue = square[x][y]

    for i in range(x, x+l):
        for j in range(y, y+l):
            if square[i][j] != isBlue:
                return False

    if isBlue: blue += 1
    else: white += 1
    return True

def divide_if_not_square(x, y, l):
    l = l//2
    next_xs = (x, x+l)
    next_ys = (y, y+l)
    
    for next_x in next_xs:
        for next_y in next_ys:
            if not check_and_add(next_x, next_y, l):
                divide_if_not_square(next_x, next_y, l)

if not check_and_add(0, 0, n):
    divide_if_not_square(0, 0, n)
print(white, blue, sep = '\n')
