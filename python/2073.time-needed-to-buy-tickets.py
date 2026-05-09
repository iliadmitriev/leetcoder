from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        t = 0
        top = tickets[k]

        for i, tick in enumerate(tickets):
            if tick >= top - (i > k):
                t += top - (i > k)
            else:
                t += tick

        return t

