

class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 1000000007

        dp = [0, 0, 0, 0, 0, 1]
        for _ in range(n):
            dp = [dp[1], dp[2], sum(dp) % MOD, dp[4], dp[5], sum(dp[3:]) % MOD]

        return sum(dp) % MOD

