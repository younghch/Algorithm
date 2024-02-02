# https://www.acmicpc.net/problem/11758

import sys
import math

class Point:
    def __init__(self, line: str):
        self.x, self.y = map(int, line.split())

def main():
    input_ = sys.stdin.readline
    points = [Point(input_()) for _ in range(3)]
    print(clockwise_or_counter_clockwise(points[0], points[1], points[2]))


def slope(p1:Point, p2:Point):
    return (p1.y-p2.y)/(p1.x-p2.x)

def distance_from_linear_function(p1:Point, p2:Point, p3:Point):
    return p3.y-(slope(p1, p2)*(p3.x-p1.x)+p1.y)

def clockwise_or_counter_clockwise(p1:Point, p2:Point, p3:Point):
    direction = None
    if (p1.x == p2.x == p3.x or p1.y == p2.y == p3.y):
        direction = 0
    elif (p1.x == p2.x):
        direction = (p2.y-p1.y)*(p1.x-p3.x)
    else:
        direction = distance_from_linear_function(p1, p2, p3)*(p2.x-p1.x)
    return 0 if direction == 0 else 1 if direction > 0 else -1

main()