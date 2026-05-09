import math


class Solution:
    def minimumSize(self, nums: list[int], maxOperations: int) -> int:
        total = sum(nums)
        count = len(nums)

        if count + maxOperations >= total:
            return 1

        def canDivide(th: int) -> bool:
            """Check if pile can be split into parts not greater than `th`.

            Find out is it enough operations to split all the balls into parts
            not greater than `th`.
            """
            ops = 0

            for n in nums:
                ops += math.ceil(n / th) - 1

                if ops > maxOperations:
                    return False

            return True

        lo = math.ceil(total / (maxOperations + count)) - 1
        hi = min(max(nums) + 1, math.ceil(total / maxOperations) + 1)

        res = lo

        while lo < hi:
            mid = (lo + hi) // 2

            if canDivide(mid):
                hi = mid
                res = mid
            else:
                lo = mid + 1

        return res

