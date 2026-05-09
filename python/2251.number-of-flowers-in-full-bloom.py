from operator import itemgetter
from heapq import heapify, heappop


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        res = [0] * len(people)
        people = sorted((p, i) for i, p in enumerate(people))
        count = 0
        start = list(map(itemgetter(0), flowers))
        end = list(map(itemgetter(1), flowers))
        heapify(start)
        heapify(end)

        for p, i in people:
            while start and start[0] <= p:
                heappop(start)
                count += 1

            while end and end[0] < p:
                heappop(end)
                count -= 1

            res[i] = count

        return res