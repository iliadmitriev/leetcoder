from collections import Counter


class Solution:
    def countBadPairs(self, nums: list[int]) -> int:
        cache = Counter(num - i for i, num in enumerate(nums))

        n = len(nums)
        total = n * (n - 1)
        good = sum(c * (c - 1) for c in cache.values())

        return (total - good) // 2

