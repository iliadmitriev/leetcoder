from collections import deque
from itertools import product
from typing import List


class Solution:
    def dfs(
        self,
        grid: list[list[int]],
        row: int,
        col: int,
        maxGold: int,
        visited: set[tuple[int, int]],
    ) -> int:
        if (
            row < 0
            or row >= len(grid)
            or col < 0
            or col >= len(grid[0])
            or (row, col) in visited
            or grid[row][col] == 0
        ):
            return 0

        visited.add((row, col))
        res = max(
            self.dfs(grid, row - 1, col, maxGold, visited),
            self.dfs(grid, row + 1, col, maxGold, visited),
            self.dfs(grid, row, col - 1, maxGold, visited),
            self.dfs(grid, row, col + 1, maxGold, visited),
        )
        visited.discard((row, col))
        return res + grid[row][col]

    def bfs(
        self, grid: list[list[int]], row: int, col: int, visited: set[tuple[int, int]]
    ) -> None:
        q = deque([(row, col)])
        visited.add((row, col))
        while q:
            row, col = q.popleft()
            for nrow, ncol in (
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ):
                if (
                    nrow < 0
                    or nrow >= len(grid)
                    or ncol < 0
                    or ncol >= len(grid[0])
                    or (nrow, ncol) in visited
                    or grid[nrow][ncol] == 0
                ):
                    continue

                visited.add((nrow, ncol))
                q.append((nrow, ncol))

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        maxGold = 0

        ROWS, COLS = len(grid), len(grid[0])
        visited: set[tuple[int, int]] = set()

        for row, col in product(range(ROWS), range(COLS)):

            maxGold = max(maxGold, self.dfs(grid, row, col, 0, visited))

        return maxGold

