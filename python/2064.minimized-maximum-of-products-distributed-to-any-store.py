

import math


class Solution:
    @staticmethod
    def checkDistribute(n: int, quantities: list[int], maxBucket: int) -> bool:
        return sum(math.ceil(q / maxBucket) for q in quantities) <= n

    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
        total = sum(quantities)
        lo, hi = max(1, total // n), max(quantities)

        while lo < hi:
            mid = (lo + hi) // 2
            if self.checkDistribute(n, quantities, mid):
                hi = mid
            else:
                lo = mid + 1

        return lo

