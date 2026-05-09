class Solution:
    def minCapability(self, nums: list[int], k: int) -> int:

        def checkGTE(nums: list[int], k: int, cap: int) -> bool:
            prev2, prev1, cur = 0, 0, 0

            for num in nums:
                cur = max(prev2 + int(num <= cap), prev1)

                if cur >= k:
                    return True

                prev2, prev1 = prev1, cur

            return False

        lo, hi = min(nums), max(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if checkGTE(nums, k, mid):
                hi = mid
            else:
                lo = mid + 1

        return lo

