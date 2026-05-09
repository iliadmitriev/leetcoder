from collections import defaultdict


class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        n = len(nums)
        pairs = defaultdict(int)

        for i in range(n):
            for j in range(i + 1, n):
                pairs[nums[i] * nums[j]] += 1

        res = 0
        for count in pairs.values():
            res += count * (count - 1)

        return res * 4

