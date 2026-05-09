class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = (
            (1, 2), (1, -2), (-1, 2), (-1, -2),
            (2, 1), (2, -1), (-2, 1), (-2, -1)
        )
        mid = ceil(n / 2)

        @cache
        def dfs(i, j, move):
            if not (0 <= i < n and 0 <= j < n):
                return 0

            if move == k:
                return 1

            # symmetry optimiztion
            if i > j or i >= mid or j >= mid:
                if i > j: i, j = j, i
                i, j = min(i, n - 1 - i), min(j, n - 1 - j)
                return dfs(i, j, move)

            return sum(
                dfs(i + di, j + dj, move + 1)
                for di, dj in directions
            ) / 8

        return dfs(row, column, 0)
