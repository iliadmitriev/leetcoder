from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        res = 0

        coverage = 0
        i = 0

        while coverage < n:
            while i < len(nums) and coverage < n and coverage + 1 >= nums[i]:
                coverage += nums[i]
                i += 1

            if coverage >= n:
                return res

            res += 1
            coverage += coverage + 1

        return res

