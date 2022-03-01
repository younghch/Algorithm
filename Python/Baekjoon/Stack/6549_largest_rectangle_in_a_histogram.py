'''
https://www.acmicpc.net/problem/6549
University of Ulm Local Contest 2003, problem H
'''
import sys

input_ = sys.stdin.readline

def get_largest(hist):
    stack = []
    largest = 0

    for h in hist:
        if not stack or stack[-1][0] < h:
            stack.append([h, 1])
        elif stack[-1][0] == h:
            stack[-1][1] += 1
        else:
            last = stack.pop()
            width = last[1]
            while stack and stack[-1][0] > h:
                cur = stack.pop()
                largest = max(largest, last[0]*width)
                width += cur[1]
                last = cur
                
            largest = max(largest, last[0]*width)
            if stack and stack[-1][0] == h:
                stack[-1][1] += width+1
            else:
                stack.append([h, width+1])

    last = stack.pop()
    width = last[1]
    while stack:
        cur = stack.pop()
        largest = max(largest, last[0]*width)
        width += cur[1]
        last = cur
    largest = max(largest, last[0]*width)
    
    return largest

while True:
    hist = map(int, input_().split())
    n = next(hist)
    if not n:
        exit(0)
    print(get_largest(hist))
