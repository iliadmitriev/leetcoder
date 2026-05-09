import functools


class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = int(1e9 + 7)

        @functools.cache
        def dp(n: int, i: int) -> int:
            if n == 0:
                return 1

            if n < 0 or pow(i, x) > n:
                return 0

            res = 0
            next = pow(i, x)

            res += dp(n - next, i + 1)
            res += dp(n, i + 1)

            return res % MOD

        return dp(n, 1)

