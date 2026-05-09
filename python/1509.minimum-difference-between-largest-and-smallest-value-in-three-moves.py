
from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)

        if len(nums) < 5:
            return 0

        nums.sort()

        return min(nums[n - 4 + k] - nums[k] for k in range(4))

