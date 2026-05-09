class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]
        maxLen = 0

        for num in nums:
            num %= k

            for j in range(k):
                dp[num][j] = dp[j][num] + 1
                maxLen = max(maxLen, dp[num][j])

        return maxLen

