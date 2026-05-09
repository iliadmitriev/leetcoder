class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7

        arrLen = min(steps + 1, arrLen)
        
        @cache
        def dp(steps: int, pos: int) -> int:
            if pos >= arrLen or pos < 0 or steps < 0:
                return 0

            if pos == 0 and steps == 0:
                return 1

            res = dp(steps - 1, pos + 1) + dp(steps - 1, pos - 1) + dp(steps - 1, pos)
            return res % MOD


        return dp(steps, 0)