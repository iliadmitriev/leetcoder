import collections


class Solution:
    def maxDifference(self, s: str) -> int:
        cnt = collections.Counter(s)

        a1 = max(v for v in cnt.values() if v % 2 == 1)
        a2 = min(v for v in cnt.values() if v % 2 == 0)

        return a1 - a2

