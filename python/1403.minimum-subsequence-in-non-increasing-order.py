class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        total = sum(nums)
        nums.sort(reverse=True)

        acc = 0

        for i in range(len(nums)):
            acc += nums[i]
            if acc > total - acc:
                return nums[: i + 1]

        return nums

