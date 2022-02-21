'''
https://www.acmicpc.net/problem/1541
'''

import sys

input_ = sys.stdin.readline

equation = input_().rstrip()
isMinus = False
cur_num = 0
sum_ = 0

for c in equation:
    if isMinus and c in ('+', '-'):
        sum_ -= cur_num
        cur_num = 0
    elif c in ('+', '-'):
        if c == '-':
            isMinus = True
        sum_ += cur_num
        cur_num = 0
    else:
        cur_num = cur_num*10+int(c)
sum_ += -cur_num if isMinus else cur_num

print(sum_)

# Better solution

# acc = [sum(map(int, x.split('+'))) for x in input_().rstrip().split('-')]
# print(acc[0]-sum(acc[1:]))