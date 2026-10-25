from queue import deque


class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs_fill(r: int, c: int):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != 0:
                return

            grid[r][c] = 1

            dfs_fill(r + 1, c)
            dfs_fill(r - 1, c)
            dfs_fill(r, c + 1)
            dfs_fill(r, c - 1)


        for r in range(m):
            dfs_fill(r, 0)
            dfs_fill(r, n - 1)

        for c in range(n):
            dfs_fill(0, c)
            dfs_fill(m - 1, c)
        
        res = 0
        for r in range(1, m - 1):
            for c in range(1, n - 1):
                if grid[r][c] == 0:
                    res += 1
                    dfs_fill(r, c)

        return res
