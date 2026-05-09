from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        cache = set()
        res = -1
        for n in nums:
            if -n in cache:
                if res < abs(n):
                    res = abs(n)
            cache.add(n)
        return res

