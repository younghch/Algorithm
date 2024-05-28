# https://leetcode.com/problems/move-zeroes

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zero_start = 0
        non_zero_start = 0

        while non_zero_start < n:
            while zero_start < n and nums[zero_start] != 0:
                zero_start += 1
            if zero_start == n:
                break

            non_zero_start = zero_start

            while non_zero_start < n and nums[non_zero_start] == 0:
                non_zero_start += 1
            if non_zero_start == n:
                break

            for i in range(0, non_zero_start - zero_start):
                try:
                    nums[zero_start + i], nums[non_zero_start + i] = nums[non_zero_start + i], nums[zero_start + i]
                except IndexError:
                    break
            


        