import collections


class Solution:
    def countTrapezoids(self, points: list[list[int]]) -> int:
        MOD = int(1e9 + 7)
        # count number of points on each line parallel to x axis
        counter = collections.Counter(y for _, y in points)

        total = 0
        result = 0

        for p in counter.values():
            edges = p * (p - 1) // 2

            result += edges * total
            result %= MOD

            total += edges
            total %= MOD

        return result

