"""
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

"""
from typing import *


class Solution:
    def mySqrt(self, x: int) -> int:
        flag = True
        i = 0
        while flag:
            i += 1
            if i * i > x:
                flag = False
                continue
            if i * i == x:
                return i
        return i - 1

