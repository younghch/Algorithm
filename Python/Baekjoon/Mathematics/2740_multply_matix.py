'''
https://www.acmicpc.net/problem/2740
'''
import sys

input_ = sys.stdin.readline

n, m = map(int, input_().split())
a = [tuple(map(int, input_().split())) for _ in range(n)]
_, k = map(int, input_().split())
b = [tuple(map(int, input_().split())) for _ in range(m)]

def multiply(l, r):
    res = 0
    for v_left, v_right in zip(l, r):
        res += v_left*v_right
    return res

def multiply_matrix(a, b):
    ans = []
    for l in a:
        temp = []
        for r in zip(*b):
            temp.append(str(multiply(l, r)))
        ans.append(temp)
    return ans

print(*map(' '.join, multiply_matrix(a, b)), sep='\n')
