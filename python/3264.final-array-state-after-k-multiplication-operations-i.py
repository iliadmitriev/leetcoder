import heapq


class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:

        hq = [(v, i) for i, v in enumerate(nums)]
        heapq.heapify(hq)

        for _ in range(k):
            _, i = heapq.heappop(hq)

            nums[i] *= multiplier
            heapq.heappush(hq, (nums[i], i))

        return nums

