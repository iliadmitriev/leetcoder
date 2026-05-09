import functools


class Solution:
    def minimumDistance(self, word: str) -> int:
        n = len(word)

        def dist(a: str, b: str) -> int:
            p1 = ord(a) - ord("A")
            p2 = ord(b) - ord("A")

            width = 6
            r1, c1 = p1 // width, p1 % width
            r2, c2 = p2 // width, p2 % width

            return abs(r1 - r2) + abs(c1 - c2)

        @functools.cache
        def dp(i: int = -1, j: int = -1) -> int:
            i, j = max(i, j), min(i, j)

            if i == n - 1:
                return 0

            d1 = (
                dist(word[i], word[i + 1]) if i >= 0 else 0
            )  # distance without switching
            d2 = (
                dist(word[j], word[i + 1]) if j >= 0 else 0
            )  # distance to switch finger

            return min(
                d1 + dp(i + 1, j),
                d2 + dp(i + 1, i),
            )

        return dp()
