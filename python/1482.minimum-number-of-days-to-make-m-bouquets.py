from typing import List


class Solution:
    def canMakeBouquets(self, bloomDay: List[int], mid: int, m: int, k: int) -> bool:
        j = 0
        for i in range(len(bloomDay)):
            if bloomDay[i] <= mid:
                j += 1
                if j == k:
                    j = 0
                    m -= 1
            else:
                j = 0

            if m == 0:
                break

        return m <= 0

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        lo = min(bloomDay)
        hi = max(bloomDay)

        while lo < hi:
            mid = (lo + hi) // 2
            if self.canMakeBouquets(bloomDay, mid, m, k):
                hi = mid
            else:
                lo = mid + 1

        return lo

