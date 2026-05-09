class Solution:
    def maxSum(self, nums: list[int]) -> int:
        uniq = set(num for num in nums if num >= 0)
        if len(uniq) == 0:
            return max(nums)

        return sum(uniq)

