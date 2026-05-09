class Solution:
    def maxAdjacentDistance(self, nums: list[int]) -> int:
        n = len(nums)

        maxAbs = abs(nums[0] - nums[n - 1])
        for i in range(1, n):
            maxAbs = max(maxAbs, abs(nums[i] - nums[i - 1]))

        return maxAbs

