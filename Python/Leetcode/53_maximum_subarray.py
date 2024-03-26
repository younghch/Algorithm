# https://leetcode.com/problems/maximum-subarray
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_max = nums[0]
        sum_current = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            sum_current = max(sum_current+num, num)
            sum_max = max(sum_current, max)
        return sum_max