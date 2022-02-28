'''
https://www.acmicpc.net/problem/10830
'''
import sys

input_ = sys.stdin.readline

n, b = map(int, input_().split())
a = [list(map(lambda x: x%1000, list(map(int, input_().split())))) for _ in range(n)]

def multiply(row, col):
    res = 0
    for r, c in zip(row, col):
        res = (res+r*c)%1000
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

def print_matrix(a):
    for line in a:
        print(*line, sep=' ')

print_matrix(power_matrix(a, b))
