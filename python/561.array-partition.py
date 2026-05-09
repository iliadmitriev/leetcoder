class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        totalMax = 0

        for i in range(0, n, 2):
            totalMax += nums[i]

        return totalMax

