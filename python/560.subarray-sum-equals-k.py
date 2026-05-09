
import collections


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        acc = 0
        cache = collections.defaultdict(int)
        cache[0] = 1

        total = 0

        for num in nums:
            acc += num
            total += cache[acc - k]
            cache[acc] += 1

        return total

