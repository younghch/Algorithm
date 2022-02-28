'''
https://www.acmicpc.net/problem/11444
'''
import sys

input_ = sys.stdin.readline

n = int(input_())
fibo = [[1, 1], [1, 0]]
r = [[1, 1], [1, 0]]

def multiply(row, col):
    res = 0
    for r, c in zip(row, col):
        res = (res+r*c)%1000000007
    return res

def multply_matrix(m1, m2):
    res = [[multiply(row, col) for col in zip(*m2)] for row in m1]
    return res

def power_matrix(a, b):
    if b == 1:
        return a
    half = power_matrix(a, b//2)
    half_square = multply_matrix(half, half)
    return half_square if b%2 == 0 else multply_matrix(half_square, a)

if n <= 2:
    fibo = [0, 1, 1]
    print(fibo[n])
else:
    print(multply_matrix(fibo, power_matrix(r, n-2))[0][0])
