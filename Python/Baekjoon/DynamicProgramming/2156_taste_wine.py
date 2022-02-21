'''
https://www.acmicpc.net/problem/2156
'''

import sys

input_ = sys.stdin.readline

n = int(input_())
amounts = [int(input_()) for _ in range(n)]

def getMaxAmount(n):
    acc = [[0, 0, 0] for _ in range(n)]
    #not selected, selected but not selected before, selected & selected
    acc[0] = [0, amounts[0], 0]
    acc[1] = [amounts[0], amounts[1], amounts[0]+amounts[1]]
    for i in range(2, n):
        amount = amounts[i]
        acc[i] = [max(max(acc[i-1]), max(acc[i-2])), acc[i-1][0]+amount, acc[i-1][1]+amount]
    return max(acc[n-1])

if n < 3:
    print(sum(amounts))
else:
    print(getMaxAmount(n))
