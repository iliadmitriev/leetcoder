import numpy as np


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = int(1e9) + 7

        A = np.array(nums, dtype=np.int64)

        for l, r, k, v in queries:
            A[l : r + 1 : k] = A[l : r + 1 : k] * v % MOD

        return int(np.bitwise_xor.reduce(A))
