class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        n = len(nums)
        left = [0] * n
        right = [0] * n

        for i in range(1, n):
            left[i] = left[i - 1] + nums[i - 1]
            right[n - i - 1] = right[n - i] + nums[n - i]

        for i in range(n):
            nums[i] = abs(left[i] - right[i])

        return nums

