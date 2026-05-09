class Solution:
    def numSubmat(self, mat: list[list[int]]) -> int:
        total = 0
        m, n = len(mat), len(mat[0])

        heights = [0] * n

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0

            stack = -1
            dp = [0] * n
            for j in range(n):
                while stack >= 0 and heights[stack] >= heights[j]:
                    stack -= 1

                prev = dp[stack] if stack >= 0 else 0

                dp[j] = prev + (j - stack) * heights[j]

                stack = j
                total += dp[j]

        return total

