from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        max_square = 0
        dp = [[int(matrix[i][j]) for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0 and dp[i][j]:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],
                        dp[i - 1][j - 1],
                        dp[i][j - 1],
                    )

                max_square = max(max_square, dp[i][j])

        return max_square**2

