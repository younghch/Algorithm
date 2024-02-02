# https://www.acmicpc.net/problem/11758

import sys

class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __sub__(self, other):
        return Vector(self.x-other.x, self.y-other.y)
    
    def cross_product(self, other):
        return self.x*other.y-other.x*self.y
    
def main():
    input_ = sys.stdin.readline
    points = [Vector(*map(int, input_().split())) for _ in range(3)]
    print(clockwise_or_counter_clockwise(points[0], points[1], points[2]))

def clockwise_or_counter_clockwise(v1:Vector, v2:Vector, v3:Vector):
    direction = (v2-v1).cross_product(v3-v2)
    return 0 if direction == 0 else 1 if direction > 0 else -1

main()