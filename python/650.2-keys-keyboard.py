from functools import cache


class Solution:
    def minSteps(self, n: int) -> int:
        """ """
        INF = 10**9

        @cache
        def dp(count: int, paste: int) -> int:
            if count == n:
                return 0

            if count > n:
                return INF

            # paste previous copy
            paste = 1 + dp(count + paste, paste)

            # copy and then paste (cant just copy,
            # falldown to infinite loop of copying)
            copyPaste = 2 + dp(2 * count, count)

            return min(paste, copyPaste)

        # corner case
        if n == 1:
            return 0

        return 1 + dp(1, 1)

