'''
https://www.acmicpc.net/problem/4949
'''

import sys

input_ = sys.stdin.readline

def getValid(s):
    stack = []
    isValid = True
    for c in s:
        if c == '(':
            stack.append(0)
        elif c == ')':
            if len(stack) == 0 or stack.pop() != 0:
                isValid = False
                break
        elif c == '[':
            stack.append(1)
        elif c == ']':
            if len(stack) == 0 or stack.pop() != 1:
                isValid = False
                break
    if stack or not isValid:
        return 'no'
    return 'yes'
    
while True:
    s = input_().rstrip()
    if s == '.':
        exit(0)
    print(getValid(s))
