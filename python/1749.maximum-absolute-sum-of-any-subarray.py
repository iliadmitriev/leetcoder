class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        maxSum, curMaxSum = 0, 0
        minSum, curMinSum = 0, 0

        for num in nums:
            curMaxSum += num
            curMinSum += num

            curMaxSum = max(curMaxSum, 0)
            maxSum = max(maxSum, curMaxSum)

            curMinSum = min(curMinSum, 0)
            minSum = min(minSum, curMinSum)

        return max(abs(maxSum), abs(minSum))

