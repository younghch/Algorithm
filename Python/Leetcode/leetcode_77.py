"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

You may return the answer in any order.
"""
import itertools
from typing import *


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        def dfs(elements, start, k):
            if k == 0:
                results.append(elements[:])

            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()

        dfs([], 1, k)
        return results

    def combine2(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1, n + 1), k))


s = Solution()
print(s.combine(4, 2))
print(s.combine2(4, 2))