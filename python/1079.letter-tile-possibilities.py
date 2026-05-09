from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        chars = [0] * 26
        for c, n in Counter(tiles).items():
            chars[ord(c) - ord("A")] = n

        def backtrack(chars):
            total = 0

            for i in range(26):
                if not chars[i]:
                    continue

                total += 1

                chars[i] -= 1
                total += backtrack(chars)
                chars[i] += 1

            return total

        return backtrack(chars)

