
from bisect import bisect_right
from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        start = newInterval[0]
        start_idx = bisect_right(intervals, start, key=lambda x: x[0])

        intervals.insert(start_idx, newInterval)

        res = []
        for interval in intervals:
            if res and res[-1][1] >= interval[0]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)

        return res

