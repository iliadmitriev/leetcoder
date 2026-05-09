import functools


class Solution:
    def minScoreTriangulation(self, values: list[int]) -> int:
        n = len(values)

        @functools.cache
        def dp(i: int, j: int) -> int:
            if j - i < 2:
                return 0

            if j - i == 2:
                return values[i] * values[i + 1] * values[j]

            return min(
                values[i] * values[k] * values[j] + dp(i, k) + dp(k, j)
                for k in range(i + 1, j)
            )

        return dp(0, n - 1)

