class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        count = 0

        right = sum(nums)
        left = 0

        for i in range(len(nums) - 1):
            left += nums[i]
            right -= nums[i]
            if left >= right:
                count += 1

        return count

