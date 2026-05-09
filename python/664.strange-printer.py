from functools import cache


class Solution:
    def strangePrinter(self, s: str) -> int:
        # compress string removing duplicates
        z: list[str] = []
        for i in range(len(s)):
            if i == 0 or s[i - 1] != s[i]:
                z.append(s[i])

        @cache
        def dp(left: int, right: int) -> int:

            if left > right:
                return 0

            # worst case: all letter are different:
            # we use one turn to print first one
            # and proceed with subproblem
            minTurns = 1 + dp(left + 1, right)

            # better cases: find matches of letters
            # and decide one of them which is less turns
            for i in range(left + 1, right + 1):
                if z[i] == z[left]:
                    turns = dp(left, i - 1) + dp(i + 1, right)
                    minTurns = min(minTurns, turns)

            return minTurns

        return dp(0, len(z) - 1)

