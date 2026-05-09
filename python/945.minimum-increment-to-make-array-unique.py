from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        res = 0
        prev = -1
        nums.sort()

        for i in range(len(nums)):
            if prev < nums[i]:
                prev = nums[i]
                continue

            diff = prev - nums[i] + 1
            res += diff
            prev = nums[i] + diff
        return res

