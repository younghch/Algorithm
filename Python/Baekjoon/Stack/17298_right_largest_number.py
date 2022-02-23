'''
https://www.acmicpc.net/problem/17298
'''

import sys

input_ = sys.stdin.readline

n = int(input_())
a = list(map(int, input_().split()))
stack = [a[n-1]]
rev_seq = [-1]

for i in range(n-2, -1, -1):
    cur = a[i]
    top = stack[-1]
    while cur >= top:
        stack.pop()
        if not stack:
            break
        top = stack[-1]
    if not stack:
        rev_seq.append(-1)
    else:
        rev_seq.append(top)
    stack.append(cur)

print(*rev_seq[::-1])
