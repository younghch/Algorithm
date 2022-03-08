'''
https://www.acmicpc.net/problem/1655
'''
import sys, heapq

input_ = sys.stdin.readline

n = int(input_())
max_heap = []
min_heap = []

def add(x):
    middle_left = -max_heap[0]
    middle_right = min_heap[0]
    if len(max_heap) == len(min_heap):
        if x > middle_right:
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
            heapq.heappush(min_heap, x)
        else:
            heapq.heappush(max_heap, -x)
    else:
        if x < middle_left:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
            heapq.heappush(max_heap, -x)
        else:
            heapq.heappush(min_heap, x)

if n == 1:
    print(int(input_()))
else:
    first = int(input_())
    second = int(input_())
    max_heap.append(-min(first, second))
    min_heap.append(max(first, second))
    to_print = [first, -max_heap[0]]

    for _ in range(n-2):
        add(int(input_()))
        to_print.append(-max_heap[0])

    print(*to_print, sep='\n')
    