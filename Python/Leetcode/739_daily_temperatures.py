# https://leetcode.com/problems/daily-temperatures
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack: List[Temperature] = list()
        for i in range(len(temperatures)):
            temperature = temperatures[i]
            while len(stack) != 0 and stack[-1].temperature < temperature:
                past_record = stack.pop()
                answer[past_record.idx] = i - past_record.idx
            stack.append(Temperature(temperature, i))
        return answer

class Temperature:
    def __init__(self, temperature, idx) -> None:
        self.temperature = temperature;
        self.idx = idx

