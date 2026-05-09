from collections import Counter


class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        pairs = Counter(nums)

        res = [0, 0]
        for v in pairs.values():
            res[0] += v // 2
            res[1] += v % 2

        return res

