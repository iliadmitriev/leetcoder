from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        acc = 0
        cache = {0: 0}

        for i, n in enumerate(nums, start=1):

            acc += n
            acc %= k

            if acc not in cache:
                cache[acc] = i
            elif cache[acc] <= i - 2:
                return True

        return False

