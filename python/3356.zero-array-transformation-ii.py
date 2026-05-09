class Solution:
    def minZeroArray(self, nums: list[int], queries: list[list[int]]) -> int:

        def lessThanZero(arr: list[int], q: list[list[int]], k: int) -> bool:
            n = len(arr)

            prefix = [0] * (n + 1)

            for i in range(k):
                a, b, v = q[i]
                prefix[a] += v
                prefix[b + 1] -= v

            cur = 0
            for i in range(n):
                cur += prefix[i]
                if arr[i] > cur:
                    return False

            return True

        res = -1
        lo, hi = 0, len(queries) + 1

        while lo < hi:

            mid = (lo + hi) // 2

            if lessThanZero(nums, queries, mid):
                hi = mid
                res = mid
            else:
                lo = mid + 1

        return res

