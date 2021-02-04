"""
Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.
"""
from typing import *
import collections


# work but slow
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = dict()
        for char in t:
            if char in target.keys():
                target[char].append(-1)
            else:
                target[char] = collections.deque([-1])
        all_in = False
        shortest = float('inf')
        ans = None
        for i in range(len(s)):
            if s[i] in target.keys():
                target[s[i]].popleft()
                target[s[i]].append(i)
                if all_in is False:
                    all_in = True
                    for values in target.values():
                        for value in values:
                            if value == -1:
                                all_in = False
                                break
                        if all_in is False:
                            break
                if all_in is True:
                    starts, ends = [], []
                    for values in target.values():
                        starts.append(values[0])
                        ends.append(values[-1])
                    start, end = min(starts), max(ends)
                    if end - start < shortest:
                        shortest = end - start
                        ans = (start, end)
        if ans is not None:
            return s[ans[0]:ans[1] + 1]
        return ""

    def minWindow2(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        missing = len(t)
        left = start = end = 0
        for right, char in enumerate(s, 1):
            missing -= need[char] > 0
            need[char] -= 1

        if missing == 0:
            while left < right and need[s[left]] < 0:
                need[s[left]] += 1
                left += 1
            if not end or right - left <= end - start:
                start, end = left, right
                need[s[left]] += 1
                missing += 1
                left += 1
            return s[start:end]
s = Solution()
print(s.minWindow2("ADOBECODEBANC", "ABC"))
