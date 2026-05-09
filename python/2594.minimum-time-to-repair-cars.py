import math


class Solution:
    def repairCars(self, ranks: list[int], cars: int) -> int:
        def isTimeEnough(ranks: list[int], cars: int, lim: int) -> bool:
            for rank in ranks:
                cars -= int(math.sqrt(lim // rank))
                if cars <= 0:
                    return True

            return False

        m = len(ranks)
        lo, hi = 0, (cars // m + 1) ** 2 * max(ranks)

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if isTimeEnough(ranks, cars, mid):
                hi = mid
            else:
                lo = mid + 1

        return lo

