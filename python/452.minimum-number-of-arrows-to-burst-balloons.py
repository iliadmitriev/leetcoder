from operator import itemgetter
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=itemgetter(1))
        counter = 0
        prev_end = -float("inf")

        for start, end in points:
            if start > prev_end:
                counter += 1
                prev_end = end

        return counter

