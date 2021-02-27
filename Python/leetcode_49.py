"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

from typing import *
import collections


class Solution:
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        words = collections.defaultdict(list)

        # make w1, w2 always be sorted
        def check_anagram(w1, w2):
            if len(w1) != len(w2):
                return False
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    return False
            return True

        for word in strs:
            sorted_w = tuple(sorted(word))
            is_new = True
            for key in words.keys():
                if check_anagram(key, sorted_w):
                    is_new = False
                    words[key].append(word)
                    break
            if is_new:
                words[sorted_w].append(word)
        return words.values()

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return anagrams.values()


s = Solution()
print(s.groupAnagrams1(["eat", "tea", "tan", "ate", "nat", "bat"]))
