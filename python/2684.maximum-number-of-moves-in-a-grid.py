class Solution:
    def maxMoves(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1

        maxMoves = 0

        for j in range(1, n):
            for i in range(m):
                if grid[i][j - 1] < grid[i][j] and dp[i][j - 1] > 0:
                    dp[i][j] = max(dp[i][j], dp[i][j - 1] + 1)

                if (
                    i - 1 >= 0
                    and grid[i - 1][j - 1] < grid[i][j]
                    and dp[i - 1][j - 1] > 0
                ):
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)

                if (
                    i + 1 < m
                    and grid[i + 1][j - 1] < grid[i][j]
                    and dp[i + 1][j - 1] > 0
                ):
                    dp[i][j] = max(dp[i][j], dp[i + 1][j - 1] + 1)

                maxMoves = max(maxMoves, dp[i][j] - 1)

        return maxMoves

