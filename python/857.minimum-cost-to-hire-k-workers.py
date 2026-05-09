class Solution:
    def mincostToHireWorkers(
        self, quality: List[int], wage: List[int], k: int
    ) -> float:

        rate = map(lambda x, y: x / y, wage, quality)
        if k == len(quality):
            return sum(quality) * max(rate)

        # cost of one unit of quality
        data = sorted(zip(rate, quality))

        hq: list[int] = list(-q for _, q in data[:k])
        heapify(hq)

        curQuality = -sum(hq)
        minCost = curQuality * data[k - 1][0]

        for newRate, newQuality in data[k:]:
            oldQuality = -heappushpop(hq, -newQuality)
            curQuality += newQuality - oldQuality
            minCost = min(minCost, newRate * curQuality)

        return minCost
