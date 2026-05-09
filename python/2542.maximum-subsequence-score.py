from operator import itemgetter
from heapq import heapify, heappop, heappush

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        if k == n:
            return sum(nums1) * min(nums2)

        data = sorted(zip(nums2, nums1), key=itemgetter(1), reverse=True)

        hq = data[:k]
        curSum = sum(map(itemgetter(1), hq))
        heapify(hq)
        factor = hq[0][0]

        res = curSum * factor

        for i in range(k, n):
            curSum -= heappop(hq)[1]
            curSum += data[i][1]
            heappush(hq, data[i])
            factor = hq[0][0]

            res = max(res, curSum * factor)

        return res