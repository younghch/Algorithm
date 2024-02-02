# https://www.acmicpc.net/problem/11758

import sys

class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    
def main():
    input_ = sys.stdin.readline
    points = [Vector(*map(int, input_().split())) for _ in range(3)]
    print(clockwise_or_counter_clockwise(points[0], points[1], points[2]))

def clockwise_or_counter_clockwise(v1:Vector, v2:Vector, v3:Vector):
    v_first = minus_vector(v1, v2)
    v_second = minus_vector(v2, v3)
    direction = cross_product(v_first, v_second)
    return 0 if direction == 0 else 1 if direction > 0 else -1

def cross_product(v1:Vector, v2:Vector):
    return v1.x*v2.y-v2.x*v1.y

def minus_vector(v1: Vector, v2:Vector):
    return Vector(v1.x-v2.x, v1.y-v2.y)

main()