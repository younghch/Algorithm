# https://leetcode.com/problems/non-overlapping-intervals
from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key = lambda interval: interval[1])
        pickeds = [sorted_intervals[0]]
        for interval in sorted_intervals:
            if not is_overlapps(interval, pickeds[-1]):
                pickeds.append(interval)
        return len(intervals) - len(pickeds)

def is_overlapps(interval1, interval2):
    i1_start, i1_end = interval1[0], interval1[1]
    i2_start, i2_end = interval2[0], interval2[1]
    return i1_start <= i2_start < i1_end or i1_start < i2_end <= i1_end