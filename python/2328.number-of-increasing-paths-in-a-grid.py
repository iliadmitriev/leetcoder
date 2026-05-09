from itertools import product

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        mod = 10**9 + 7

        m, n = len(grid), len(grid[0])

        dp = [[1] * n for _ in range(m)]

        steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # build linear array of cell indexes
        cells = product(range(m), range(n))
        # sort ascending by grid values
        cells_list = sorted(cells, key=lambda cell: grid[cell[0]][cell[1]])

        for i, j in cells_list:
            for dy, dx in steps:
                r, c = i + dy, j + dx
                if 0 <= r < m and 0 <= c < n \
                    and grid[r][c] > grid[i][j]:
                        dp[r][c] += dp[i][j]
                        dp[r][c] %= mod

        return sum(sum(dp, [])) % mod
