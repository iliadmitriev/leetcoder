class Solution:
    def countPartitions(self, nums: list[int]) -> int:
        n = len(nums)
        left = 0
        right = sum(nums)
        counter = 0

        for i in range(n - 1):
            left += nums[i]
            right -= nums[i]

            counter += (left - right) % 2 == 0

        return counter

