from collections import defaultdict


class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        cache: defaultdict[int, int] = defaultdict(int)
        count = 0

        for num in nums:
            count += cache[num - k] + cache[num + k]
            cache[num] += 1

        return count

