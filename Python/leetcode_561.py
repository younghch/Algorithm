"""
Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.
"""

from typing import *


class Solution:
    def arrayPairSum1(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        for i in range(0, len(nums), 2):
            ans += nums[i]
        return ans

    def arrayPairSum2(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
