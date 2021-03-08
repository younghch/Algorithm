"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
"""

from typing import *


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [nums[0]]
        right = [nums[len(nums) - 1]]
        ans = []
        for i in range(1, len(nums)):
            left.append(left[i - 1] * nums[i])
        for j in range(1, len(nums)):
            right.append(right[j - 1] * nums[len(nums) - 1 - j])
        right = right[::-1]
        ans.append(right[1])
        for k in range(1, len(nums) - 1):
            ans.append(left[k - 1] * right[k + 1])
        ans.append(left[-2])
        return ans


s = Solution()
s.productExceptSelf([1,2,3,4])