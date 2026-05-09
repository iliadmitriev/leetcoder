from functools import cache


class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        n = len(s)

        @cache
        def dp(pos: int) -> int:
            if pos == n:
                return 0

            res = 1 + dp(pos + 1)

            for word in dictionary:
                if s[pos: pos + len(word)] == word:
                    res = min(res, dp(pos + len(word)))

            return res

        return dp(0)

