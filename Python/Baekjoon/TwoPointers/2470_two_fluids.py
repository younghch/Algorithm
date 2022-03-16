'''
https://www.acmicpc.net/problem/2470
'''
import sys

input_ = sys.stdin.readline

input_()
numbers = sorted(map(int, input_().split()))

def two_pointers_min_diff():
    s, e = 0, len(numbers)-1
    pair = [None, None]
    diff = float('inf')
    while s < e:
        n_diff = numbers[s]+numbers[e]
        if abs(n_diff) < abs(diff):
            diff = n_diff
            pair = (numbers[s], numbers[e])
            if diff == 0:
                break
        if n_diff > 0:
            e -= 1
        else:
            s += 1
    return pair

print(*two_pointers_min_diff())

