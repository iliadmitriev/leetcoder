from collections.abc import Iterator


class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        def prefix(num: int) -> Iterator[tuple[int, int]]:
            res = str(num)
            for i in range(1, len(str(num)) + 1):
                yield i, int(res[:i])

        cache = set()
        for num1 in arr1:
            for _, pref in prefix(num1):
                cache.add(pref)

        maxPrefixLen = 0
        for num in arr2:

            for ll, pref in prefix(num):
                if pref in cache:
                    maxPrefixLen = max(maxPrefixLen, ll)

        return maxPrefixLen


