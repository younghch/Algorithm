# https://leetcode.com/problems/increasing-triplet-subsequence
from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')
        for num in nums:
            if first >= num:
                first = num
            elif second > num:
                second = num
            elif num > second: 
                return True
        return False

solution = Solution()

assert solution.increasingTriplet([1,2,3,4,5]) == True
assert solution.increasingTriplet([3,2,1,3,2,1]) == False