class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n < 2:
            return n

        dp = [0] * (n + 1)
        dp[0], dp[1] = 0, 1
        ans = 1

        for i in range(1, n // 2 + 1):

            dp[i * 2] = dp[i]
            ans = max(ans, dp[2 * i])

            if i * 2 + 1 <= n:
                dp[i * 2 + 1] = dp[i] + dp[i + 1]
                ans = max(ans, dp[i * 2 + 1])

        return ans

