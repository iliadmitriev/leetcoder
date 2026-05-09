class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for length in range(1, n):  # start sliding window lenght from 1 up to n - 1
            for l in range(0, n - length): # start from 0 and moves up to (n - length) end of string minus length of sliding window
                r = l + length # start from length of sliding window and moves up to n - 1 (end of string)
                if s[l] == s[r]:
                    dp[l][r] = dp[l + 1][r - 1]
                else:
                    dp[l][r] = min(dp[l + 1][r], dp[l][r - 1]) + 1
        
        return dp[0][-1]
