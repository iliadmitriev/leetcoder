from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums

        counter = Counter(nums)
        return heapq.nlargest(k, counter.keys(), key=counter.get)