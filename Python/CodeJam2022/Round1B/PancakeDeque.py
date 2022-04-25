import sys
from collections import deque

input_ = sys.stdin.readline

t = int(input_())
to_print = []

def get_numer_of_possible_customers(pancakes):
    last = 0
    count = 0
    while pancakes:
        is_left_first = True
        if pancakes[0] > pancakes[-1]:
            is_left_first = False
        if is_left_first:
            cur = pancakes.popleft()
            if cur >= last:
                last = cur
                count += 1
        else:
            cur = pancakes.pop()
            if cur >= last:
                last = cur
                count += 1
    return count
        

for i in range(t):
    n = int(input_())
    pancakes = deque(map(int, input_().split()))
    to_print.append(f'Case #{i+1}: {get_numer_of_possible_customers(pancakes)}')

print('\n'.join(to_print))
