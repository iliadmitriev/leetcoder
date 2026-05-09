import heapq
import math


class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        gifts = [-gift for gift in gifts]
        heapq.heapify(gifts)

        for _ in range(k):
            heapq.heappush(gifts, -int(math.sqrt(-heapq.heappop(gifts))))

        return sum(-g for g in gifts)

