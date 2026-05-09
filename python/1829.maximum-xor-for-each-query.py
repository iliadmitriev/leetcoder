import operator
from functools import reduce


class Solution:
    def getMaximumXor(self, nums: list[int], maximumBit: int) -> list[int]:
        res = []
        allXor = reduce(operator.xor, nums, 0)
        k = (1 << maximumBit) - 1

        while nums:
            res.append(allXor ^ k)
            allXor ^= nums.pop()

        return res

