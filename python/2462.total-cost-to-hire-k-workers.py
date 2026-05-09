import heapq


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        if 2 * candidates >= len(costs):
            return sum(heapq.nsmallest(k, costs))

        head, tail = costs[:candidates], costs[-candidates:]
        free = costs[candidates:][:-candidates]

        heapify(head)
        heapify(tail)
        top = lambda x: x[0] if x else float("inf")
        res = []

        for _ in range(k):
            if top(head) <= top(tail):
                worker = heapq.heappop(head)
                if free:
                    heapq.heappush(head, free.pop(0))
            else:
                worker = heapq.heappop(tail)
                if free:
                    heapq.heappush(tail, free.pop(-1))

            res.append(worker)

        return sum(res)

        
