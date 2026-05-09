from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        if k == len(nums):
            return k

        i = 0
        cnt = {}
        res = 0

        for j in range(len(nums)):

            cnt[nums[j]] = cnt.get(nums[j], 0) + 1

            while i <= j and cnt.get(nums[j], 0) > k:
                cnt[nums[i]] -= 1
                i += 1

            res = max(res, j - i + 1)

        return res

