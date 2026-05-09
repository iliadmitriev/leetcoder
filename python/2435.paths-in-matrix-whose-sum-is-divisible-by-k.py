import functools


class Solution:
    def numberOfPaths(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        MOD = int(1e9 + 7)

        @functools.cache
        def backtrack(r, c, s):
            if r >= m or c >= n:
                return 0

            if r == m - 1 and c == n - 1:
                return int(s % k == 0)

            res = 0

            for dr, dc in [(0, 1), (1, 0)]:
                nr, nc = r + dr, c + dc
                if nr >= m or nc >= n:
                    continue

                res += backtrack(nr, nc, (s + grid[nr][nc]) % k)
                res %= MOD

            return res

        # return backtrack(0, 0, grid[0][0] % k)

        dp = [[0] * k for _ in range(n + 1)]
        dp[1][0] = 1

        for r in range(m):
            for c in range(n):
                dpn = [0] * k
                for s in range(k):
                    ns = (s + grid[r][c]) % k

                    dpn[s] = (dp[c + 1][ns] + dp[c][ns]) % MOD

                dp[c + 1] = dpn

        return dp[n][0]

