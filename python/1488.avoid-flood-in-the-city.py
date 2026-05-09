import collections
import heapq


class Solution:
    def avoidFlood(self, rains: list[int]) -> list[int]:
        n = len(rains)
        hq = []
        future = collections.defaultdict(collections.deque)
        res = [1] * n
        flood = set()

        for i, r in enumerate(rains):
            future[r].append(i)

        for i in range(n):
            if rains[i] == 0:
                if hq:
                    _, lake = heapq.heappop(hq)
                    res[i] = lake
                    flood.discard(lake)

            else:
                lake = rains[i]

                future[rains[i]].popleft()

                res[i] = -1
                if lake in flood:
                    return []

                flood.add(lake)
                if future[lake]:
                    heapq.heappush(hq, (future[lake][0], lake))

        return res

