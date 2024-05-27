# https://leetcode.com/problems/smallest-number-in-infinite-set
import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.recently_popped = 0
        self.add_backed = []

    def popSmallest(self) -> int:
        if not self.add_backed:
            self.recently_popped += 1
            return self.recently_popped
        else:
            to_return = heapq.heappop(self.add_backed)
            while self.add_backed and self.add_backed[0] == to_return:
                heapq.heappop(self.add_backed)
            return to_return

    def addBack(self, num: int) -> None:
        if self.recently_popped >= num:
            heapq.heappush(self.add_backed, num)
            
            
# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)