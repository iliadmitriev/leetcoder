import operator
from functools import reduce


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        x = reduce(operator.mul, nums)
        return (x > 0) - (x < 0)