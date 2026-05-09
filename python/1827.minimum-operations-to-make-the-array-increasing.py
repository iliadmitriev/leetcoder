class Solution:
    def minOperations(self, nums: list[int]) -> int:
        ops = 0

        n = len(nums)
        value = nums[0]

        for i in range(1, n):
            if value >= nums[i]:
                value += 1
                ops += value - nums[i]
            else:
                value = nums[i]

        return ops

