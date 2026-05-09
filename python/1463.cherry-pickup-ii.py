class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """
        Time: O(ROW_NUM * COL_NUM * COL_NUM)
        Space: O(ROW_NUM * COL_NUM * COL_NUM)
        """
        # save number of rows and cols (minimum is 2 by the condition of problem)
        m, n = len(grid), len(grid[0])

        if n == 2:
            return sum(sum(row) for row in grid)
        elif n == 3:
            return sum(sum(row) - min(row) for row in grid)
        
        # previous row cache dp[i][j], i - left , j - right
        # (only upper right part, for reducing computations, diagonal symmetry)
        dp = [[0] * n for _ in range(n)]

        for r in reversed(range(m)):
            cur_dp = [[0] * n for _ in range(n)]
            # use c1, c2 - for column indexes for left and right robot
            # c1 < c2
            for c1 in range(0, n - 1):
                for c2 in range(c1 + 1, n):
                    res = 0
                    for d1, d2 in product((-1, 0, 1), repeat=2):
                        if c1 + d1 < 0 or c2 + d2 >= n:
                            continue

                        res = max(res, dp[c1 + d1][c2 + d2])

                    cur_dp[c1][c2] = res + grid[r][c1] + grid[r][c2]
            dp = cur_dp

        return dp[0][n - 1]

                        
