import operator as op
from functools import reduce
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        out = reduce(op.xor, nums) ^ k
        return out.bit_count()

