class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        
        Operations:
            - insert
            - delete
            - replace
            
        Idea:
        
        if not equal:
            d[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        else:
            d[i][j] = dp[i - 1][j - 1]
        
                a   b   c   d   e   f
            0   1   2   3   4   5   6
        a   1   0   1   2   3   4   5
        z   2   1   1   2   3   4   5
        c   3   2   2   1   2   3   4
        e   4   3   3   2   2   2   3
        d   5   4   4   3   2   3   3
                                   ---
        
        """
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1) ]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],
                        dp[i - 1][j - 1],
                        dp[i][j - 1]
                    )
        return dp[m][n]