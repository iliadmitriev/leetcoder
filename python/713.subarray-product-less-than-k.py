from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        prod = 1
        p, q = 0, 0

        while q < len(nums):

            prod *= nums[q]

            while p <= q and prod >= k:
                prod //= nums[p]
                p += 1

            res += q - p + 1
            q += 1

        return res

