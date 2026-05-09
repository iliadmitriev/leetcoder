class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0.0] * (n + maxPts)

        for i in range(k, n + 1):
            dp[i] = 1.0

        S = min(n - k + 1, maxPts)

        for i in range(k - 1, -1, -1):
            dp[i] = S / maxPts
            S += dp[i] - dp[i + maxPts]

        return dp[0]