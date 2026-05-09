class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        dist = abs(startPos - endPos)

        # optimize 1: if finish mark is even and number of steps odd (or other vise)
        # finish is unreachable
        # optimize 2: if the finish is beyond the number of steps (not enough steps)
        # finish is unreachable
        if dist % 2 != k % 2 or dist > k:
            return 0


        MOD = 10**9 + 7

        @cache
        def dp(distance: int, steps: int) -> int:
            if steps < 0:
                return 0

            if distance == 0 and steps == 0:
                return 1

            res = dp(distance - 1, steps - 1) + dp(distance + 1, steps - 1)
            return res % MOD

        return dp(dist, k)