from collections import Counter
from heapq import heapify, heappop
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        counts = Counter(hand)
        heapCounts = list(counts.keys())
        heapify(heapCounts)

        while heapCounts:
            minCount = heapCounts[0]
            for i in range(minCount, minCount + groupSize):
                if counts.get(i, 0) == 0:
                    return False
                counts[i] -= 1
                if counts[i] == 0:
                    if heapCounts[0] != i:
                        return False
                    heappop(heapCounts)

        return True

