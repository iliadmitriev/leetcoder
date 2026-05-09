class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        if k > sum(candies):
            return 0

        def check(cand: list[int], v: int, k: int) -> bool:

            for c in cand:
                k -= c // v

                if k <= 0:
                    break

            return k <= 0

        res = 0
        lo, hi = 1, max(candies) + 1

        while lo < hi:
            mid = (lo + hi) // 2

            if check(candies, mid, k):
                res = mid
                lo = mid + 1
            else:
                hi = mid

        return res

