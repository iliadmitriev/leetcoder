import math


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:

        def calc_min_time(dist: List[int], speed: int):
            time = 0.0
            for d in dist:
                time = math.ceil(time)
                time += d / speed
            return time

        lo, hi = 1, 10**9

        if calc_min_time(dist, hi) > hour:
            return -1

        while lo < hi:
            mid = (lo + hi) // 2

            if calc_min_time(dist, mid) > hour:
                lo = mid + 1
            else:
                hi = mid

        return lo
