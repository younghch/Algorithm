# https://leetcode.com/problems/optimal-partition-of-string
class Solution:
    def partitionString(self, s: str) -> int:
        ans = 1
        appeared = set()
        for c in s:
            if c in appeared:
                ans += 1
                appeared = set()
            appeared.add(c)
        return ans
