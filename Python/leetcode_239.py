"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.
"""
from typing import *
import collections


class Solution:
    # Brute force : time limit exceeded
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        for i in range(0,len(nums) - k + 1):
            max_v = nums[i]
            for j in range(i + 1, i + k):
                if nums[j] > max_v:
                    max_v = nums[j]
            ans.append(max_v)
        return ans

    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        results = []
        window = collections.deque()
        current_max = float('-inf')
        for i, v in enumerate(nums):
            window.append(v)
            if i < k - 1:
                continue
            if current_max == float('-inf'):
                current_max = max(window)
            elif v > current_max:
                current_max = v
            results.append(current_max)

            if current_max == window.popleft():
                current_max = float('-inf')

        return results
