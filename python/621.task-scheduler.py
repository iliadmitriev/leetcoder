
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = 0
        q = deque()
        hq = list(map(lambda x: -x, Counter(tasks).values()))
        heapify(hq)

        while hq or q:

            if hq:
                item = heappop(hq)
                item += 1

                if item < 0:
                    q.append((item, counter + n))

            if q and q[0][1] <= counter:
                item, _ = q.popleft()
                heappush(hq, item)

            counter += 1

        return counter

