from typing import List


class Solution:
    def find2min_idx(self, arr: List[int]) -> tuple[int, int]:
        """Finds the indexes of 2 smallest numbers in arr."""
        i1, i2 = -1, -1
        min1, min2 = float("inf"), float("inf")
        for i, el in enumerate(arr):
            if min1 > el:
                i2, min2 = i1, min1
                i1, min1 = i, el
            elif min2 > el:
                i2, min2 = i, el

        return i1, i2

    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        height, width = len(grid), len(grid[0])

        if height == 1:
            return grid[0][0]

        dp = [0] * width
        for j in range(height):
            i1, i2 = self.find2min_idx(dp)
            dp_new = grid[j].copy()

            for i in range(width):
                if i != i1:
                    dp_new[i] += dp[i1]
                else:
                    dp_new[i] += dp[i2]

            dp = dp_new

        return min(dp)

