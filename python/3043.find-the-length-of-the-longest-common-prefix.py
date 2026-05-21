import math


class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:

        cache: set[int] = set()
        for num in arr1:
            while num > 0:
                cache.add(num)
                num //= 10

        maxPrefixLen = 0
        for num in arr2:
            while num > 0:
                if num in cache:
                    maxPrefixLen = max(maxPrefixLen, int(math.log10(num)) + 1)
                    break
                num //= 10

        return maxPrefixLen

