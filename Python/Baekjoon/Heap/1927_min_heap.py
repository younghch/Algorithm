'''
https://www.acmicpc.net/problem/1927
'''
import sys, heapq

input_ = sys.stdin.readline

n = int(input_())
heap = []
to_print = []

for _ in range(n):
    if not (x := int(input_())):
        to_print.append(heapq.heappop(heap) if heap else 0)
    else:
        heapq.heappush(heap, x)

print(*to_print, sep='\n')
