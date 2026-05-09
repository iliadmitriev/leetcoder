import functools


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        """"""
        t1 = [ord(c) for c in s1]
        t2 = [ord(c) for c in s2]
        m, n = len(t1), len(t2)

        @functools.cache
        def dfs(i: int, j: int) -> int:
            if i == m or j == n:
                return sum(t1[i:m]) + sum(t2[j:n])

            if t1[i] == t2[j]:
                return dfs(i + 1, j + 1)
            else:
                return min(
                    t1[i] + dfs(i + 1, j),
                    t2[j] + dfs(i, j + 1),
                )

        # return dfs(0, 0)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + t1[i - 1]

        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] + t2[j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if t1[i - 1] == t2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        t1[i - 1] + dp[i - 1][j],
                        t2[j - 1] + dp[i][j - 1],
                    )

        return dp[m][n]

