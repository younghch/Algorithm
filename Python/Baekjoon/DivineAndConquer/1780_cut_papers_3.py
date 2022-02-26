'''
https://www.acmicpc.net/problem/1780
'''
import sys

input_ = sys.stdin.readline

n =  int(input_())
square = [input_().rstrip().split() for _ in range(n)]
count_minus = 0
count_zero = 0
count_one = 0

def check_all_same(x, y, l):
    global count_minus
    global count_zero
    global count_one

    cur = square[x][y]
    for n_x in range(x, x+l):
        for n_y in range(y, y+l):
            if cur != square[n_x][n_y]:
                return False
    match cur:
        case '-1': count_minus += 1
        case '0': count_zero += 1
        case '1': count_one += 1
    return True
    
def split_three(x, y, l):
    if check_all_same(x, y, l):
        return
    l = l//3
    xs = (x, x+l, x+l*2)
    ys = (y, y+l, y+l*2)

    for n_x in xs:
        for n_y in ys:
            if not check_all_same(n_x, n_y, l):
                split_three(n_x, n_y, l)

split_three(0, 0, n)
print(count_minus, count_zero, count_one, sep='\n')
