class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = int(1e9 + 7)

        dp = [0] * (high + 1)

        for i in range(high, -1, -1):

            dp[i] = int(i >= low)

            dp[i] += dp[i + zero] if i + zero <= high else 0

            dp[i] += dp[i + one] if i + one <= high else 0

            dp[i] %= MOD

        return dp[0]

