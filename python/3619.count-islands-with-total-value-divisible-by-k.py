class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> int:

            res = grid[r][c]
            grid[r][c] = 0

            if r + 1 < m and grid[r + 1][c] != 0:
                res += dfs(r + 1, c)
            
            if c + 1 < n and grid[r][c + 1] != 0:
                res += dfs(r, c + 1)

            if r - 1 >= 0 and grid[r - 1][c] != 0:
                res += dfs(r - 1, c)

            if c - 1 >= 0 and grid[r][c - 1] != 0:
                res += dfs(r, c - 1)

            return res

        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    continue

                res = dfs(r, c)
                if res % k == 0:
                    count += 1

        return count
        