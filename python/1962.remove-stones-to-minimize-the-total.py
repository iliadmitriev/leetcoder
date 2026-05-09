from heapq import heapify, heappop, heappush
from math import floor


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        hq = list(map(lambda x: -x, piles))
        heapify(hq)

        for _ in range(k):
            if hq[0] == -1:
                break
            pile = -heappop(hq)
            pile -= floor(pile / 2)
            heappush(hq, -pile)

        return -sum(hq)