class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        mod = 10**9 + 7
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1
        
        for i in reversed(range(n)):
            if s[i] == '0':
                continue

            j = i + 1
            count = 0
            while int(s[i:j], 10) <= k and j <= len(s):
                dp[i] += dp[j]
                j += 1
            dp[i] %= mod

        return dp[0]