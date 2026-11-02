import numpy as np


class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        a = np.array(nums)
        n = len(a)
        med = np.partition(a, n // 2)[n // 2]

        return int(np.abs(a - med).sum())
