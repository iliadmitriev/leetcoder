import collections


class Solution:
    def findLucky(self, arr: list[int]) -> int:
        return max(
            (k for k, v in collections.Counter(arr).items() if k == v),
            default=-1,
        )

