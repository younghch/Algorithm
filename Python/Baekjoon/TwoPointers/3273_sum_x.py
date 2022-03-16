'''
https://www.acmicpc.net/problem/3273
'''
import sys

input_ = sys.stdin.readline

input_()
numbers = sorted(map(int, input_().split()))
x = int(input_())

def two_pointer():
    count = 0
    s, e = 0, len(numbers)-1
    while e > s:
        sum_ = numbers[s]+numbers[e]
        if sum_ > x:
            e -= 1
        elif sum_ < x:
            s += 1
        else:
            count += 1
            s += 1
    return count
    
print(two_pointer())
