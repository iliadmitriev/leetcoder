from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = 0
        ones, zeroes = 0, 0

        dp = {0: -1}

        for i in range(len(nums)):
            if nums[i] == 1:
                ones += 1
            else:
                zeroes += 1

            if ones - zeroes in dp:
                res = max(res, i - dp[ones - zeroes])
            else:
                dp[ones - zeroes] = i

        return res

