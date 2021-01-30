"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
"""

import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = heapq.heapify(nums)
        for _ in range(len(nums) - 1):
            heapq.heappop(heap)
        return heapq.heappop(heap)

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

    def findKthLargest3(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]