# https://www.acmicpc.net/problem/25308

import sys
import math

is_convex = dict()

class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def __sub__(self, other):
        return Vector(self.x-other.x, self.y-other.y)
    
    def __mul__(self, n:int):
        return Vector(n*self.x, n*self.y)
    
    def cross_product(self, other):
        return self.x*other.y-other.x*self.y


def update_is_convex(a1:int, a2:int, a3:int, abilities: list[int]):
    if (a1, a2, a3) in is_convex:
        return

    i = Vector(0, 1)*a1
    j = Vector(math.sqrt(0.5), math.sqrt(0.5))*a2
    k = Vector(1, 0)*a3

    convex = (j-i).cross_product(k-j) < 0
    is_convex[(a1, a2, a3)] = convex
    if not convex:
        for i in range(abilities.index(a3)+1, len(abilities)):
            is_convex[(a1, a2, abilities[i])] = False

def dfs(last, current, to_visit:list[int]):
    count = 0
    if len(to_visit) == 2:
        if is_convex[(last, current, to_visit[0])] and is_convex[(current, to_visit[0], to_visit[1])]:
            count += 1 
    else:
        num_not_to_iter = 1 if last is None else 2
        for i in range(len(to_visit)-num_not_to_iter):
            next_ = to_visit[i]
            if last is None:
                to_visit.append(next_)

            if last is None or is_convex[(last, current, next_)]:
                to_visit.pop(i)
                count += dfs(current, next_, to_visit)
                to_visit.insert(i, next_)

            if last is None:
                to_visit.pop()

    return count


def main():
    input_ = sys.stdin.readline
    abilities = sorted(map(int, input_().split()))
    for a1 in abilities:
        for a2 in abilities:
            for a3 in abilities:
                update_is_convex(a1, a2, a3, abilities)

    start = abilities[0]
    to_visit = [*abilities[1:], start]
    print(dfs(None, start, to_visit)*8)

if __name__ == '__main__':
    main()
