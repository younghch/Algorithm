# https://www.acmicpc.net/problem/2166
from typing import List
import sys

class Point:
    def __init__(self, raw_string:str):
        self.x, self.y = map(int, raw_string.split())

def main():
    input_ = sys.stdin.readline

    n = int(input_())
    points = [Point(input_()) for _ in range(n)]
    print(shoelace(points))

def shoelace(points: List[Point]):
    n = len(points)
    area:int = 0
    for i in range(n):
        area += determinant(points[i], points[(i+1)%n])
    return abs(area)

def determinant(p1:Point, p2:Point):
    return (p1.x*p2.y-p2.x*p1.y)/2
    
main()
