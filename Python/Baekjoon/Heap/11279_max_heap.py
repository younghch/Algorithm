'''
https://www.acmicpc.net/problem/11279

My MaxHeap class returns 0 when heap is empty according to problem's condition.
Using a heapq module is the fastest but used my own class to study.
'''
import sys

input_ = sys.stdin.readline

class MaxHeap():
    def __init__(self):
        self.items = [None]

    def __len__(self):
        return len(self.items)-1

    def push(self, item):
        self.items.append(item)
        idx = len(self)
        parent = idx//2
        while parent > 0:
            if self.items[parent] < self.items[idx]:
                self.items[idx], self.items[parent] = self.items[parent], self.items[idx]
                idx = parent
                parent = idx//2
            else:
                return
    
    def pop(self):
        if len(self) == 0:
            return 0
        extracted = self.items[1]
        self.items[1] = self.items[len(self)]
        self.items.pop()
        idx = 1
        child_left = idx*2
        while child_left <= len(self):
            largest = idx
            if self.items[child_left] > self.items[largest]:
                largest = child_left
            if child_left+1 <= len(self) and self.items[child_left+1] > self.items[largest]:
                largest = child_left+1
            if largest != idx:
                self.items[idx], self.items[largest] = self.items[largest], self.items[idx]
                idx = largest
                child_left = idx*2
            else:
                break
    
        return extracted
         
n = int(input_())
heap = MaxHeap()
to_print = []

for _ in range(n):
    x = int(input_())
    if not x:
        to_print.append(heap.pop())
    else:
        heap.push(x)

print(*to_print, sep='\n')
