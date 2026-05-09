class Solution:
    def maxRunTime(self, n: int, batteries: list[int]) -> int:
        def check(t: int) -> bool:
            total = 0
            for b in batteries:
                total += min(b, t)

                if total >= n * t:
                    return True

            return False

        lo = 1
        hi = sum(batteries) // n + 1
        res = 0

        while lo < hi:
            mid = (lo + hi) // 2

            if check(mid):
                res = mid
                lo = mid + 1
            else:
                hi = mid

        return res

