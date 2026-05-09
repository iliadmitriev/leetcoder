class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        prev = 0
        curSum = 0
        maxSum = 0

        for num in nums:
            if prev < num:
                curSum += num
            else:
                curSum = num

            prev = num
            maxSum = max(maxSum, curSum)

        return maxSum

