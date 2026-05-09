from collections import defaultdict
from math import comb


class Solution:
    def countCompleteDayPairs(self, hours: list[int]) -> int:
        count24: defaultdict[int, int] = defaultdict(int)

        for h in hours:
            count24[h % 24] += 1

        return (
            comb(count24[0], 2)
            + comb(count24[12], 2)
            + sum(count24[h] * count24[24 - h] for h in range(1, 12))
        )

