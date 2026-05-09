DIR = [1, 1, -1, -1, 1]


class Solution:
    @staticmethod
    def dfs(
        grid: list[list[int]],
        dp: list[list[list[list[int]]]],
        r: int,
        c: int,
        d: int,
        t: int,
        n: int,
    ) -> int:
        if dp[r][c][d][t] != -1:
            return dp[r][c][d][t]

        ans = 1
        nr, nc = r + DIR[d], c + DIR[d + 1]

        # don't change direction
        if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]):
            if grid[nr][nc] == n:
                ans = max(ans, 1 + Solution.dfs(grid, dp, nr, nc, d, t, n ^ 2))

        # change direction
        if t == 0:
            nd = (d + 1) % 4
            nr, nc = r + DIR[nd], c + DIR[nd + 1]

            if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]):
                if grid[nr][nc] == n:
                    ans = max(ans, 1 + Solution.dfs(grid, dp, nr, nc, nd, 1, n ^ 2))

        dp[r][c][d][t] = ans
        return ans

    def lenOfVDiagonal(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[[-1] * 2 for _ in range(4)] for _ in range(n)] for _ in range(m)]

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1:
                    continue

                for d in range(4):
                    ans = max(ans, self.dfs(grid, dp, i, j, d, 0, 2))

        return ans

