from collections import deque
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        res = [-1] * n

        deck.sort()
        it = iter(deck)

        q = deque(range(n))

        while q:
            pos = q.popleft()

            if q:
                drop = q.popleft()
                q.append(drop)

            res[pos] = next(it)

        return res

