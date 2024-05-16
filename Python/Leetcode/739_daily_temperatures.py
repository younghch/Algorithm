# https://leetcode.com/problems/daily-temperatures
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack: List = list()
        for i in range(len(temperatures)):
            temperature = temperatures[i]
            while stack and temperatures[stack[-1]] < temperature:
                idx = stack.pop()
                answer[idx] = i - idx
            stack.append(i)
        return answer


