import functools


class Solution:
    def maxDotProduct(self, nums1: list[int], nums2: list[int]) -> int:
        a, b = max(nums1), min(nums2)
        if a < 0 and b > 0:
            return a * b

        c, d = min(nums1), max(nums2)
        if c > 0 and d < 0:
            return c * d

        m, n = len(nums1), len(nums2)

        @functools.cache
        def dfs(i: int, j: int) -> int:
            if i == m or j == n:
                return 0

            return max(
                nums1[i] * nums2[j] + dfs(i + 1, j + 1),
                dfs(i + 1, j),
                dfs(i, j + 1),
            )

        # return dfs(0, 0)

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = max(
                    nums1[i] * nums2[j] + dp[i + 1][j + 1],
                    dp[i + 1][j],
                    dp[i][j + 1],
                )

        return dp[0][0]

