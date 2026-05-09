import collections


class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        total = 0

        cache = collections.defaultdict(int)
        for a, b in dominoes:
            if a > b:
                a, b = b, a

            cache[(a, b)] += 1

        for v in cache.values():
            total += v * (v - 1) // 2

        return total

