import heapq


class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        hq = []

        for i, num in enumerate(nums):
            if len(hq) < k:
                heapq.heappush(hq, (num, i))
            else:
                if hq[0][0] < num:
                    heapq.heappop(hq)
                    heapq.heappush(hq, (num, i))

        return list(map(lambda x: x[0], sorted(hq, key=lambda y: y[1])))

