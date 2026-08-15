import operator
import functools

class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        zero = nums.count(0)
        if zero == len(nums):
            return 0

        total = functools.reduce(operator.xor, nums, 0)

        if total == 0:
            return len(nums) - 1

        return len(nums)
