import sys


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSum = -sys.maxsize
        curSum = 0

        for num in nums:
            curSum += num

            maxSum = max(maxSum, curSum)
            curSum = max(0, curSum)

        return maxSum

