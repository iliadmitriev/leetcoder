import functools


class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = int(1e9 + 7)

        @functools.cache
        def dp(n: int, col: str) -> int:
            if n == 0:
                return 1

            if col == "3C":
                return (2 * dp(n - 1, "3C") + 2 * dp(n - 1, "2C")) % MOD

            return (2 * dp(n - 1, "3C") + 3 * dp(n - 1, "2C")) % MOD

        return (6 * dp(n - 1, "3C") + 6 * dp(n - 1, "2C")) % MOD

