import numpy as np

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        h = len(nums) // 2
        sq = np.square(nums, dtype=np.int64)
        total = sq.sum()
        lowest_h = np.partition(sq, h)[:h].sum()

        return (total - 2 * lowest_h).item()
        